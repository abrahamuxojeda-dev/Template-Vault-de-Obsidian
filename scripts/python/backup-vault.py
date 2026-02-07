#!/usr/bin/env python3
"""
backup-vault.py
Automated backup system for Obsidian vaults

Usage:
    python backup-vault.py --vault /path/to/vault --destination ~/Backups/
    python backup-vault.py --vault /path/to/vault --destination ~/Backups/ --compress
    python backup-vault.py --vault /path/to/vault --destination ~/Backups/ --retention 30

Features:
- Full vault backup
- Incremental backups
- Compression (zip/tar.gz)
- Retention policy
- Backup verification
- Exclude patterns
"""

import argparse
import shutil
import zipfile
import tarfile
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Set
import json


class VaultBackup:
    def __init__(self, vault_path: str, destination: str):
        self.vault_path = Path(vault_path).resolve()
        self.destination = Path(destination).resolve()
        self.destination.mkdir(parents=True, exist_ok=True)
        
        # Default exclusions
        self.exclude_patterns = {
            '.obsidian/workspace*',
            '.obsidian/cache',
            '.trash',
            '.DS_Store',
            'Thumbs.db',
            '*.tmp',
            '__pycache__',
        }
        
    def create_backup(self, compress: bool = False, 
                     backup_type: str = 'full',
                     incremental_base: str = None) -> str:
        """Create a backup of the vault."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        vault_name = self.vault_path.name
        
        if compress:
            backup_name = f"{vault_name}_backup_{timestamp}.zip"
            backup_path = self.destination / backup_name
            
            print(f"🗜️  Creating compressed backup: {backup_name}")
            self.create_zip_backup(backup_path)
            
        else:
            backup_name = f"{vault_name}_backup_{timestamp}"
            backup_path = self.destination / backup_name
            
            print(f"📦 Creating backup: {backup_name}")
            
            if backup_type == 'incremental' and incremental_base:
                self.create_incremental_backup(backup_path, incremental_base)
            else:
                self.create_full_backup(backup_path)
        
        # Create backup metadata
        self.create_backup_metadata(backup_path, backup_type, timestamp)
        
        # Verify backup
        if self.verify_backup(backup_path):
            print(f"✅ Backup created successfully: {backup_path}")
            return str(backup_path)
        else:
            print(f"❌ Backup verification failed!")
            return None
    
    def create_full_backup(self, backup_path: Path):
        """Create a full backup by copying all files."""
        backup_path.mkdir(parents=True, exist_ok=True)
        
        files_copied = 0
        total_size = 0
        
        for item in self.vault_path.rglob('*'):
            if item.is_file() and not self.should_exclude(item):
                relative_path = item.relative_to(self.vault_path)
                dest_path = backup_path / relative_path
                
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_path)
                
                files_copied += 1
                total_size += item.stat().st_size
                
                if files_copied % 100 == 0:
                    print(f"  Copied {files_copied} files...", end='\r')
        
        print(f"\n  📁 Copied {files_copied} files ({self.format_size(total_size)})")
    
    def create_incremental_backup(self, backup_path: Path, base_backup: str):
        """Create incremental backup (only changed files)."""
        base_path = Path(base_backup)
        
        if not base_path.exists():
            print(f"⚠️  Base backup not found, creating full backup instead")
            return self.create_full_backup(backup_path)
        
        backup_path.mkdir(parents=True, exist_ok=True)
        
        files_copied = 0
        files_skipped = 0
        
        for item in self.vault_path.rglob('*'):
            if item.is_file() and not self.should_exclude(item):
                relative_path = item.relative_to(self.vault_path)
                dest_path = backup_path / relative_path
                base_file = base_path / relative_path
                
                # Check if file changed
                if self.file_changed(item, base_file):
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, dest_path)
                    files_copied += 1
                else:
                    # Create hardlink to save space
                    dest_path.parent.mkdir(parents=True, exist_ok=True)
                    if base_file.exists():
                        try:
                            dest_path.hardlink_to(base_file)
                            files_skipped += 1
                        except:
                            shutil.copy2(item, dest_path)
                            files_copied += 1
                
                if (files_copied + files_skipped) % 100 == 0:
                    print(f"  Processed {files_copied + files_skipped} files...", end='\r')
        
        print(f"\n  📁 Copied {files_copied} new/changed files, linked {files_skipped} unchanged")
    
    def create_zip_backup(self, backup_path: Path):
        """Create compressed zip backup."""
        files_added = 0
        
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for item in self.vault_path.rglob('*'):
                if item.is_file() and not self.should_exclude(item):
                    arcname = item.relative_to(self.vault_path)
                    zipf.write(item, arcname)
                    files_added += 1
                    
                    if files_added % 100 == 0:
                        print(f"  Added {files_added} files...", end='\r')
        
        print(f"\n  📦 Compressed {files_added} files")
        print(f"  💾 Backup size: {self.format_size(backup_path.stat().st_size)}")
    
    def should_exclude(self, path: Path) -> bool:
        """Check if path should be excluded from backup."""
        relative_path = str(path.relative_to(self.vault_path))
        
        for pattern in self.exclude_patterns:
            if Path(relative_path).match(pattern):
                return True
        
        return False
    
    def file_changed(self, file1: Path, file2: Path) -> bool:
        """Check if file has changed (by modification time and size)."""
        if not file2.exists():
            return True
        
        stat1 = file1.stat()
        stat2 = file2.stat()
        
        # Compare size and modification time
        if stat1.st_size != stat2.st_size:
            return True
        
        if abs(stat1.st_mtime - stat2.st_mtime) > 1:  # 1 second tolerance
            return True
        
        return False
    
    def create_backup_metadata(self, backup_path: Path, backup_type: str, timestamp: str):
        """Create metadata file for backup."""
        metadata = {
            'timestamp': timestamp,
            'backup_type': backup_type,
            'vault_path': str(self.vault_path),
            'vault_name': self.vault_path.name,
            'created': datetime.now().isoformat(),
            'files_count': self.count_files(backup_path),
            'total_size': self.get_directory_size(backup_path),
        }
        
        metadata_file = backup_path.parent / f"{backup_path.name}_metadata.json"
        metadata_file.write_text(json.dumps(metadata, indent=2))
    
    def verify_backup(self, backup_path: Path) -> bool:
        """Verify backup integrity."""
        if backup_path.suffix == '.zip':
            try:
                with zipfile.ZipFile(backup_path, 'r') as zipf:
                    corrupt = zipf.testzip()
                    if corrupt:
                        print(f"⚠️  Corrupt file in backup: {corrupt}")
                        return False
                return True
            except Exception as e:
                print(f"❌ Error verifying zip: {e}")
                return False
        else:
            # For directory backups, just check if it exists and has files
            return backup_path.exists() and self.count_files(backup_path) > 0
    
    def apply_retention_policy(self, days: int):
        """Delete backups older than specified days."""
        print(f"\n🗑️  Applying retention policy ({days} days)...")
        
        cutoff_date = datetime.now() - timedelta(days=days)
        deleted_count = 0
        freed_space = 0
        
        for backup in self.destination.iterdir():
            if not backup.name.startswith(self.vault_path.name):
                continue
            
            # Get backup timestamp
            try:
                timestamp_str = backup.name.split('_backup_')[1].split('.')[0]
                backup_date = datetime.strptime(timestamp_str, "%Y%m%d_%H%M%S")
                
                if backup_date < cutoff_date:
                    size = self.get_directory_size(backup) if backup.is_dir() else backup.stat().st_size
                    
                    if backup.is_dir():
                        shutil.rmtree(backup)
                    else:
                        backup.unlink()
                    
                    # Delete metadata if exists
                    metadata_file = backup.parent / f"{backup.name}_metadata.json"
                    if metadata_file.exists():
                        metadata_file.unlink()
                    
                    deleted_count += 1
                    freed_space += size
                    
                    print(f"  Deleted: {backup.name}")
            except:
                continue
        
        if deleted_count > 0:
            print(f"✅ Deleted {deleted_count} old backups, freed {self.format_size(freed_space)}")
        else:
            print("  No old backups to delete")
    
    def list_backups(self) -> List[Dict]:
        """List all available backups."""
        backups = []
        
        for item in self.destination.iterdir():
            if item.name.startswith(self.vault_path.name) and '_backup_' in item.name:
                metadata_file = item.parent / f"{item.name}_metadata.json"
                
                if metadata_file.exists():
                    metadata = json.loads(metadata_file.read_text())
                else:
                    # Basic metadata
                    metadata = {
                        'timestamp': item.name.split('_backup_')[1].split('.')[0],
                        'created': datetime.fromtimestamp(item.stat().st_ctime).isoformat(),
                    }
                
                metadata['name'] = item.name
                metadata['path'] = str(item)
                metadata['size'] = self.get_directory_size(item) if item.is_dir() else item.stat().st_size
                
                backups.append(metadata)
        
        return sorted(backups, key=lambda x: x['timestamp'], reverse=True)
    
    def count_files(self, path: Path) -> int:
        """Count files in directory."""
        if path.is_file():
            return 1
        return sum(1 for _ in path.rglob('*') if _.is_file())
    
    def get_directory_size(self, path: Path) -> int:
        """Calculate total size of directory."""
        if path.is_file():
            return path.stat().st_size
        
        total = 0
        for item in path.rglob('*'):
            if item.is_file():
                total += item.stat().st_size
        return total
    
    def format_size(self, size: int) -> str:
        """Format size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"


def main():
    parser = argparse.ArgumentParser(description='Backup Obsidian vault')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--destination', required=True, help='Backup destination directory')
    parser.add_argument('--compress', action='store_true', help='Create compressed zip backup')
    parser.add_argument('--type', choices=['full', 'incremental'], default='full',
                       help='Backup type')
    parser.add_argument('--base', help='Base backup for incremental backup')
    parser.add_argument('--retention', type=int, help='Delete backups older than N days')
    parser.add_argument('--list', action='store_true', help='List existing backups')
    parser.add_argument('--exclude', nargs='*', help='Additional exclude patterns')
    
    args = parser.parse_args()
    
    backup = VaultBackup(args.vault, args.destination)
    
    # Add custom exclusions
    if args.exclude:
        backup.exclude_patterns.update(args.exclude)
    
    if args.list:
        # List existing backups
        print(f"\n📋 Backups in {args.destination}:\n")
        backups = backup.list_backups()
        
        if not backups:
            print("No backups found")
        else:
            for i, b in enumerate(backups, 1):
                print(f"{i}. {b['name']}")
                print(f"   Created: {b.get('created', 'Unknown')}")
                print(f"   Size: {backup.format_size(b['size'])}")
                print(f"   Files: {b.get('files_count', 'Unknown')}")
                print()
    else:
        # Create backup
        print(f"🎒 Starting backup of: {args.vault}")
        print(f"📁 Destination: {args.destination}\n")
        
        backup_path = backup.create_backup(
            compress=args.compress,
            backup_type=args.type,
            incremental_base=args.base
        )
        
        # Apply retention policy if specified
        if args.retention and backup_path:
            backup.apply_retention_policy(args.retention)
        
        print("\n✨ Backup complete!")


if __name__ == '__main__':
    main()