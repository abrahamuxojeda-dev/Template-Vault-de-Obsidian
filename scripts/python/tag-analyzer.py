#!/usr/bin/env python3
"""
tag-analyzer.py
Analyze tag usage in Obsidian vault and suggest improvements

Usage:
    python tag-analyzer.py --vault /path/to/vault
    python tag-analyzer.py --vault /path/to/vault --min-count 3
    python tag-analyzer.py --vault /path/to/vault --suggest-merges --output report.md

Features:
- Count tag usage
- Find similar/duplicate tags
- Identify orphan tags
- Suggest tag consolidation
- Generate hierarchy recommendations
"""

import argparse
import re
import yaml
from pathlib import Path
from collections import Counter, defaultdict
from typing import List, Dict, Set, Tuple
from difflib import SequenceMatcher
from datetime import datetime


class TagAnalyzer:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.tags: Counter = Counter()
        self.tag_files: Dict[str, List[str]] = defaultdict(list)
        self.hierarchical_tags: Dict[str, Set[str]] = defaultdict(set)
        
    def scan_vault(self):
        """Scan vault and collect all tags."""
        print(f"📂 Scanning vault: {self.vault_path}")
        
        markdown_files = list(self.vault_path.rglob("*.md"))
        print(f"Found {len(markdown_files)} markdown files")
        
        for file_path in markdown_files:
            try:
                content = file_path.read_text(encoding='utf-8')
                tags = self.extract_tags(content)
                
                for tag in tags:
                    self.tags[tag] += 1
                    self.tag_files[tag].append(str(file_path.relative_to(self.vault_path)))
                    
                    # Track hierarchical relationships
                    parts = tag.split('/')
                    for i in range(1, len(parts)):
                        parent = '/'.join(parts[:i])
                        child = '/'.join(parts[:i+1])
                        self.hierarchical_tags[parent].add(child)
                        
            except Exception as e:
                print(f"⚠️  Error reading {file_path}: {e}")
        
        print(f"✅ Found {len(self.tags)} unique tags")
        print(f"📊 Total tag occurrences: {sum(self.tags.values())}")
    
    def extract_tags(self, content: str) -> Set[str]:
        """Extract tags from note content."""
        tags = set()
        
        # Extract from frontmatter
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    frontmatter = yaml.safe_load(parts[1])
                    if isinstance(frontmatter, dict) and 'tags' in frontmatter:
                        fm_tags = frontmatter['tags']
                        if isinstance(fm_tags, list):
                            tags.update(tag.strip('#') for tag in fm_tags)
                        elif isinstance(fm_tags, str):
                            tags.add(fm_tags.strip('#'))
            except:
                pass
        
        # Extract inline tags (#tag)
        inline_tags = re.findall(r'#([\w/\-]+)', content)
        tags.update(inline_tags)
        
        return tags
    
    def get_tag_statistics(self) -> Dict:
        """Generate tag statistics."""
        total_tags = sum(self.tags.values())
        unique_tags = len(self.tags)
        
        return {
            'total_occurrences': total_tags,
            'unique_tags': unique_tags,
            'average_per_tag': total_tags / unique_tags if unique_tags > 0 else 0,
            'most_common': self.tags.most_common(10),
            'least_common': self.tags.most_common()[:-11:-1] if len(self.tags) > 10 else [],
            'orphan_tags': [tag for tag, count in self.tags.items() if count == 1],
        }
    
    def find_similar_tags(self, threshold: float = 0.8) -> List[Tuple[str, str, float]]:
        """Find similar tags that might be duplicates."""
        similar_pairs = []
        tag_list = list(self.tags.keys())
        
        for i, tag1 in enumerate(tag_list):
            for tag2 in tag_list[i+1:]:
                similarity = self.calculate_similarity(tag1, tag2)
                if similarity >= threshold:
                    similar_pairs.append((tag1, tag2, similarity))
        
        return sorted(similar_pairs, key=lambda x: x[2], reverse=True)
    
    def calculate_similarity(self, str1: str, str2: str) -> float:
        """Calculate similarity between two strings."""
        # Normalize
        s1 = str1.lower().replace('-', '').replace('_', '')
        s2 = str2.lower().replace('-', '').replace('_', '')
        
        return SequenceMatcher(None, s1, s2).ratio()
    
    def suggest_tag_merges(self, similar_tags: List[Tuple[str, str, float]]) -> List[Dict]:
        """Suggest which tags should be merged."""
        suggestions = []
        
        for tag1, tag2, similarity in similar_tags:
            count1 = self.tags[tag1]
            count2 = self.tags[tag2]
            
            # Suggest keeping the more common tag
            if count1 >= count2:
                keep, merge = tag1, tag2
            else:
                keep, merge = tag2, tag1
            
            suggestions.append({
                'keep': keep,
                'merge': merge,
                'similarity': similarity,
                'keep_count': self.tags[keep],
                'merge_count': self.tags[merge],
                'total_count': self.tags[keep] + self.tags[merge],
            })
        
        return suggestions
    
    def analyze_hierarchy(self) -> Dict:
        """Analyze tag hierarchy structure."""
        hierarchy_info = {
            'root_tags': [],
            'hierarchical_tags': [],
            'max_depth': 0,
            'inconsistencies': [],
        }
        
        for tag in self.tags.keys():
            depth = tag.count('/') + 1
            hierarchy_info['max_depth'] = max(hierarchy_info['max_depth'], depth)
            
            if '/' not in tag:
                hierarchy_info['root_tags'].append((tag, self.tags[tag]))
            else:
                hierarchy_info['hierarchical_tags'].append((tag, self.tags[tag], depth))
        
        # Find inconsistencies (child tags without parent)
        for tag in self.tags.keys():
            if '/' in tag:
                parts = tag.split('/')
                for i in range(1, len(parts)):
                    parent = '/'.join(parts[:i])
                    if parent not in self.tags:
                        hierarchy_info['inconsistencies'].append({
                            'tag': tag,
                            'missing_parent': parent
                        })
        
        return hierarchy_info
    
    def generate_report(self, output_path: str = None, suggest_merges: bool = False):
        """Generate comprehensive analysis report."""
        print("\n📊 Generating report...")
        
        stats = self.get_tag_statistics()
        similar_tags = self.find_similar_tags(threshold=0.75)
        hierarchy = self.analyze_hierarchy()
        
        report = f"""---
type: tag-analysis
created: {datetime.now().strftime("%Y-%m-%d %H:%M")}
tags:
  - meta
  - analysis
---

# 🏷️ Tag Analysis Report

**Generated**: {datetime.now().strftime("%Y-%m-%d %H:%M")}  
**Vault**: {self.vault_path}

---

## 📊 Overview

| Metric | Value |
|--------|-------|
| **Total Tags** | {stats['unique_tags']} |
| **Total Occurrences** | {stats['total_occurrences']} |
| **Average per Tag** | {stats['average_per_tag']:.1f} |
| **Orphan Tags** | {len(stats['orphan_tags'])} |
| **Hierarchical Tags** | {len(hierarchy['hierarchical_tags'])} |
| **Root Tags** | {len(hierarchy['root_tags'])} |
| **Max Hierarchy Depth** | {hierarchy['max_depth']} |

---

## 🔥 Most Used Tags

| Rank | Tag | Count | Usage |
|------|-----|-------|-------|
"""
        
        for i, (tag, count) in enumerate(stats['most_common'], 1):
            percentage = (count / stats['total_occurrences']) * 100
            report += f"| {i} | `{tag}` | {count} | {percentage:.1f}% |\n"
        
        report += f"""
---

## 🌱 Least Used Tags

| Tag | Count |
|-----|-------|
"""
        
        for tag, count in stats['least_common']:
            report += f"| `{tag}` | {count} |\n"
        
        report += f"""
---

## 🔍 Tag Hierarchy Analysis

### Root Tags ({len(hierarchy['root_tags'])})

| Tag | Count | Children |
|-----|-------|----------|
"""
        
        for tag, count in sorted(hierarchy['root_tags'], key=lambda x: x[1], reverse=True):
            children = len(self.hierarchical_tags.get(tag, set()))
            report += f"| `{tag}` | {count} | {children} |\n"
        
        if hierarchy['inconsistencies']:
            report += f"""
---

### ⚠️ Hierarchy Inconsistencies

Found {len(hierarchy['inconsistencies'])} tags with missing parent tags:

| Child Tag | Missing Parent |
|-----------|----------------|
"""
            
            for inconsistency in hierarchy['inconsistencies'][:20]:
                report += f"| `{inconsistency['tag']}` | `{inconsistency['missing_parent']}` |\n"
        
        if similar_tags:
            report += f"""
---

## 🔄 Similar Tags (Potential Duplicates)

Found {len(similar_tags)} similar tag pairs:

| Tag 1 | Tag 2 | Similarity | Count 1 | Count 2 |
|-------|-------|------------|---------|---------|
"""
            
            for tag1, tag2, similarity in similar_tags[:20]:
                count1 = self.tags[tag1]
                count2 = self.tags[tag2]
                report += f"| `{tag1}` | `{tag2}` | {similarity:.1%} | {count1} | {count2} |\n"
        
        if suggest_merges and similar_tags:
            merge_suggestions = self.suggest_tag_merges(similar_tags)
            
            report += f"""
---

## 💡 Merge Suggestions

Based on similarity analysis, consider these merges:

| Keep | Merge Into It | Similarity | Total Usage |
|------|---------------|------------|-------------|
"""
            
            for suggestion in merge_suggestions[:15]:
                report += f"| `{suggestion['keep']}` | `{suggestion['merge']}` | "
                report += f"{suggestion['similarity']:.1%} | "
                report += f"{suggestion['total_count']} |\n"
        
        if stats['orphan_tags']:
            report += f"""
---

## 🍃 Orphan Tags (Used Once)

{len(stats['orphan_tags'])} tags are used only once. Consider removing or consolidating:

"""
            orphan_chunks = [stats['orphan_tags'][i:i+5] for i in range(0, len(stats['orphan_tags']), 5)]
            for chunk in orphan_chunks[:10]:
                report += "- " + ", ".join(f"`{tag}`" for tag in chunk) + "\n"
            
            if len(orphan_chunks) > 10:
                report += f"\n... and {len(orphan_chunks) - 10} more groups\n"
        
        report += f"""
---

## 📋 Recommendations

### 1. Tag Consolidation
- Review similar tags and merge where appropriate
- Consider establishing naming conventions
- Use hierarchical tags consistently

### 2. Hierarchy Improvements
- Add missing parent tags for consistency
- Consider reorganizing flat tags into hierarchies
- Maximum recommended depth: 3-4 levels

### 3. Orphan Tag Cleanup
- Review single-use tags
- Either use them more or remove them
- Consider if they should be merged with existing tags

### 4. Naming Conventions
- Use lowercase for consistency
- Use hyphens or slashes consistently
- Avoid abbreviations unless standard
- Keep tags concise but descriptive

---

## 🔗 Tag Distribution by Category

"""
        
        # Group tags by first level
        categories = defaultdict(list)
        for tag, count in self.tags.items():
            category = tag.split('/')[0] if '/' in tag else tag
            categories[category].append((tag, count))
        
        for category in sorted(categories.keys(), key=lambda x: sum(c for _, c in categories[x]), reverse=True)[:10]:
            total = sum(count for _, count in categories[category])
            report += f"\n### `{category}` ({total} total uses)\n\n"
            
            for tag, count in sorted(categories[category], key=lambda x: x[1], reverse=True)[:5]:
                report += f"- `{tag}`: {count}\n"
        
        report += """
---

*This report was automatically generated. Review suggestions before making changes.*
"""
        
        if output_path:
            output_file = Path(output_path)
            output_file.write_text(report, encoding='utf-8')
            print(f"✅ Report saved to: {output_path}")
        else:
            print(report)
        
        return report


def main():
    parser = argparse.ArgumentParser(description='Analyze tags in Obsidian vault')
    parser.add_argument('--vault', required=True, help='Path to Obsidian vault')
    parser.add_argument('--output', help='Output file for report (markdown)')
    parser.add_argument('--min-count', type=int, default=1, help='Minimum tag count to include')
    parser.add_argument('--suggest-merges', action='store_true', help='Include merge suggestions')
    parser.add_argument('--similarity-threshold', type=float, default=0.75, 
                       help='Similarity threshold for finding duplicates (0.0-1.0)')
    
    args = parser.parse_args()
    
    analyzer = TagAnalyzer(args.vault)
    analyzer.scan_vault()
    
    # Filter by minimum count
    if args.min_count > 1:
        analyzer.tags = Counter({tag: count for tag, count in analyzer.tags.items() 
                                if count >= args.min_count})
    
    analyzer.generate_report(
        output_path=args.output,
        suggest_merges=args.suggest_merges
    )
    
    print("\n✨ Analysis complete!")


if __name__ == '__main__':
    main()