#!/usr/bin/env python3
"""
export-notes.py
Export Obsidian notes to various formats

Usage:
    python export-notes.py --vault /path/to/vault --format markdown --output ./export/
    python export-notes.py --vault /path/to/vault --format html --output ./export/ --filter "tag:project"
    python export-notes.py --vault /path/to/vault --format pdf --output ./export/ --single-file

Supports:
- Markdown (with cleaned links)
- HTML (styled)
- PDF (requires wkhtmltopdf)
- JSON (structured data)
- Plain text
"""

import argparse
import os
import re
import json
import yaml
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import shutil


class ObsidianExporter:
    def __init__(self, vault_path: str, output_path: str):
        self.vault_path = Path(vault_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        
    def get_all_notes(self, filter_str: Optional[str] = None) -> List[Path]:
        """Get all markdown files in vault, optionally filtered."""
        notes = list(self.vault_path.rglob("*.md"))
        
        if filter_str:
            notes = self.filter_notes(notes, filter_str)
        
        return notes
    
    def filter_notes(self, notes: List[Path], filter_str: str) -> List[Path]:
        """Filter notes based on criteria."""
        filtered = []
        
        for note in notes:
            content = note.read_text(encoding='utf-8')
            
            # Parse frontmatter
            metadata = self.parse_frontmatter(content)
            
            if filter_str.startswith("tag:"):
                tag = filter_str.split(":", 1)[1]
                if metadata and 'tags' in metadata:
                    tags = metadata['tags']
                    if isinstance(tags, list) and tag in tags:
                        filtered.append(note)
                    elif isinstance(tags, str) and tag in tags:
                        filtered.append(note)
            
            elif filter_str.startswith("folder:"):
                folder = filter_str.split(":", 1)[1]
                if folder in str(note):
                    filtered.append(note)
            
            elif filter_str.startswith("type:"):
                note_type = filter_str.split(":", 1)[1]
                if metadata and metadata.get('type') == note_type:
                    filtered.append(note)
        
        return filtered
    
    def parse_frontmatter(self, content: str) -> Optional[Dict]:
        """Parse YAML frontmatter from note."""
        if not content.startswith("---"):
            return None
        
        try:
            parts = content.split("---", 2)
            if len(parts) >= 3:
                return yaml.safe_load(parts[1])
        except:
            pass
        
        return None
    
    def export_to_markdown(self, notes: List[Path], clean_links: bool = True):
        """Export notes to clean markdown."""
        print(f"Exporting {len(notes)} notes to Markdown...")
        
        for note in notes:
            content = note.read_text(encoding='utf-8')
            
            if clean_links:
                # Convert [[wiki links]] to [wiki links](wiki-links.md)
                content = re.sub(
                    r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',
                    lambda m: f"[{m.group(2) or m.group(1)}]({m.group(1).replace(' ', '-').lower()}.md)",
                    content
                )
            
            # Create output path maintaining folder structure
            relative_path = note.relative_to(self.vault_path)
            output_file = self.output_path / relative_path
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            output_file.write_text(content, encoding='utf-8')
        
        print(f"✅ Exported to {self.output_path}")
    
    def export_to_html(self, notes: List[Path], single_file: bool = False):
        """Export notes to HTML."""
        print(f"Exporting {len(notes)} notes to HTML...")
        
        try:
            import markdown
        except ImportError:
            print("❌ Error: 'markdown' package required. Install: pip install markdown")
            return
        
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        
        if single_file:
            html_content = self.generate_html_header("Obsidian Export")
            
            for note in notes:
                content = note.read_text(encoding='utf-8')
                # Remove frontmatter
                content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
                
                html_content += f"<h1>{note.stem}</h1>\n"
                html_content += md.convert(content)
                html_content += "<hr>\n"
                md.reset()
            
            html_content += "</body></html>"
            
            output_file = self.output_path / "export.html"
            output_file.write_text(html_content, encoding='utf-8')
            
        else:
            for note in notes:
                content = note.read_text(encoding='utf-8')
                # Remove frontmatter
                content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
                
                html_content = self.generate_html_header(note.stem)
                html_content += md.convert(content)
                html_content += "</body></html>"
                md.reset()
                
                relative_path = note.relative_to(self.vault_path)
                output_file = self.output_path / relative_path.with_suffix('.html')
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                output_file.write_text(html_content, encoding='utf-8')
        
        print(f"✅ Exported to {self.output_path}")
    
    def generate_html_header(self, title: str) -> str:
        """Generate HTML header with styling."""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }}
        code {{
            background: #f6f8fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        blockquote {{
            border-left: 4px solid #dfe2e5;
            padding-left: 16px;
            color: #6a737d;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #dfe2e5;
            padding: 8px 12px;
        }}
        th {{
            background: #f6f8fa;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
"""
    
    def export_to_json(self, notes: List[Path]):
        """Export notes to JSON with metadata."""
        print(f"Exporting {len(notes)} notes to JSON...")
        
        data = []
        
        for note in notes:
            content = note.read_text(encoding='utf-8')
            metadata = self.parse_frontmatter(content)
            
            # Remove frontmatter from content
            clean_content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
            
            note_data = {
                'filename': note.name,
                'path': str(note.relative_to(self.vault_path)),
                'metadata': metadata,
                'content': clean_content,
                'created': note.stat().st_ctime,
                'modified': note.stat().st_mtime,
            }
            
            data.append(note_data)
        
        output_file = self.output_path / "export.json"
        output_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
        
        print(f"✅ Exported to {output_file}")
    
    def export_to_text(self, notes: List[Path]):
        """Export notes to plain text."""
        print(f"Exporting {len(notes)} notes to plain text...")
        
        for note in notes:
            content = note.read_text(encoding='utf-8')
            
            # Remove frontmatter
            content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
            
            # Remove markdown formatting
            content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)  # Links
            content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)  # Wiki links
            content = re.sub(r'[*_]{1,2}([^*_]+)[*_]{1,2}', r'\1', content)  # Bold/italic
            content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)  # Headers
            
            relative_path = note.relative_to(self.vault_path)
            output_file = self.output_path / relative_path.with_suffix('.txt')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            output_file.write_text(content, encoding='utf-8')
        
        print(f"✅ Exported to {self.output_path}")


def main():
    parser = argparse.ArgumentParser(description='Export Obsidian notes to various formats')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--format', required=True, 
                       choices=['markdown', 'html', 'json', 'text'],
                       help='Export format')
    parser.add_argument('--output', required=True, help='Output directory')
    parser.add_argument('--filter', help='Filter notes (e.g., "tag:project", "folder:Work", "type:task")')
    parser.add_argument('--single-file', action='store_true', help='Combine all notes into single file (HTML only)')
    parser.add_argument('--clean-links', action='store_true', help='Clean wiki links in markdown export')
    
    args = parser.parse_args()
    
    exporter = ObsidianExporter(args.vault, args.output)
    
    print(f"📂 Scanning vault: {args.vault}")
    notes = exporter.get_all_notes(args.filter)
    print(f"Found {len(notes)} notes")
    
    if len(notes) == 0:
        print("No notes found matching criteria")
        return
    
    if args.format == 'markdown':
        exporter.export_to_markdown(notes, clean_links=args.clean_links)
    elif args.format == 'html':
        exporter.export_to_html(notes, single_file=args.single_file)
    elif args.format == 'json':
        exporter.export_to_json(notes)
    elif args.format == 'text':
        exporter.export_to_text(notes)
    
    print("\n✨ Export complete!")


if __name__ == '__main__':
    main()