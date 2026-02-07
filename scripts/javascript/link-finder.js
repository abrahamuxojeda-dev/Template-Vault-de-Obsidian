/**
 * link-finder.js
 * Templater script for finding related notes based on content similarity
 * 
 * Analyzes current note and suggests related notes based on:
 * - Shared tags
 * - Common keywords
 * - Similar topics
 * - Backlinks
 * 
 * Usage: Run on any note to find connections
 */

async function find_related_notes(tp) {
    const { app } = tp;
    const activeFile = app.workspace.getActiveFile();
    
    if (!activeFile) {
        new Notice("No active file");
        return "No active file";
    }
    
    try {
        const cache = app.metadataCache.getFileCache(activeFile);
        const content = await app.vault.read(activeFile);
        
        // Extract keywords and tags
        const keywords = extractKeywords(content);
        const tags = cache?.frontmatter?.tags || [];
        const links = cache?.links?.map(link => link.link) || [];
        
        // Find similar notes
        const allFiles = app.vault.getMarkdownFiles();
        const similarities = [];
        
        for (let file of allFiles) {
            if (file.path === activeFile.path) continue;
            
            const fileCache = app.metadataCache.getFileCache(file);
            const fileContent = await app.vault.read(file);
            const fileKeywords = extractKeywords(fileContent);
            const fileTags = fileCache?.frontmatter?.tags || [];
            
            const similarity = calculateSimilarity(
                keywords,
                fileKeywords,
                tags,
                fileTags,
                links,
                file.basename
            );
            
            if (similarity.score > 0) {
                similarities.push({
                    file: file,
                    score: similarity.score,
                    reasons: similarity.reasons,
                    tags: fileTags,
                    type: fileCache?.frontmatter?.type || 'note'
                });
            }
        }
        
        // Sort by score
        similarities.sort((a, b) => b.score - a.score);
        
        // Generate report
        const report = generateReport(activeFile, similarities.slice(0, 20));
        
        // Insert at cursor or show in modal
        const insertInNote = await tp.system.prompt("Insert in note? (yes/no)");
        
        if (insertInNote === "yes") {
            return report;
        } else {
            // Create a new note with the report
            const reportFileName = `Link Suggestions - ${activeFile.basename}.md`;
            const reportPath = `_temp/${reportFileName}`;
            
            await createFolderIfNotExists(app, "_temp");
            
            const existingReport = app.vault.getAbstractFileByPath(reportPath);
            if (existingReport) {
                await app.vault.delete(existingReport);
            }
            
            await app.vault.create(reportPath, report);
            
            const reportFile = app.vault.getAbstractFileByPath(reportPath);
            if (reportFile) {
                await app.workspace.getLeaf('split').openFile(reportFile);
            }
            
            new Notice(`✅ Related notes report created`);
            return "Report created in _temp folder";
        }
        
    } catch (error) {
        new Notice(`❌ Error: ${error.message}`);
        console.error("Link finder error:", error);
        return `Error: ${error.message}`;
    }
}

function extractKeywords(content) {
    // Remove code blocks, URLs, and markdown syntax
    let cleanContent = content
        .replace(/```[\s\S]*?```/g, '')
        .replace(/`[^`]+`/g, '')
        .replace(/https?:\/\/[^\s]+/g, '')
        .replace(/[#*_\[\]()]/g, '')
        .toLowerCase();
    
    // Split into words
    const words = cleanContent.split(/\s+/);
    
    // Common stop words to exclude
    const stopWords = new Set([
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
        'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
        'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'what', 'which',
        'who', 'when', 'where', 'why', 'how', 'all', 'each', 'every', 'both',
        'few', 'more', 'most', 'other', 'some', 'such', 'not', 'only', 'own',
        'same', 'so', 'than', 'too', 'very'
    ]);
    
    // Count word frequency
    const wordFreq = {};
    for (let word of words) {
        if (word.length > 3 && !stopWords.has(word)) {
            wordFreq[word] = (wordFreq[word] || 0) + 1;
        }
    }
    
    // Get top keywords
    const keywords = Object.entries(wordFreq)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 30)
        .map(([word, freq]) => word);
    
    return keywords;
}

function calculateSimilarity(keywords1, keywords2, tags1, tags2, links, fileName) {
    let score = 0;
    const reasons = [];
    
    // Compare keywords
    const commonKeywords = keywords1.filter(k => keywords2.includes(k));
    if (commonKeywords.length > 0) {
        const keywordScore = commonKeywords.length * 2;
        score += keywordScore;
        reasons.push(`${commonKeywords.length} shared keywords`);
    }
    
    // Compare tags
    const commonTags = tags1.filter(t => tags2.includes(t));
    if (commonTags.length > 0) {
        const tagScore = commonTags.length * 5;
        score += tagScore;
        reasons.push(`${commonTags.length} shared tags: ${commonTags.slice(0, 3).join(', ')}`);
    }
    
    // Check if linked
    if (links.includes(fileName)) {
        score += 10;
        reasons.push('Already linked');
    }
    
    return { score, reasons };
}

function generateReport(activeFile, similarities) {
    const moment = window.moment;
    
    let report = `---
type: link-suggestions
source: ${activeFile.basename}
created: ${moment().format("YYYY-MM-DD HH:mm")}
tags:
  - meta
  - suggestions
---

# 🔗 Related Notes for "${activeFile.basename}"

Generated: ${moment().format("YYYY-MM-DD HH:mm")}

---

## 🎯 Summary

Found **${similarities.length}** potentially related notes.

---

## 📋 Suggestions

`;
    
    for (let i = 0; i < Math.min(similarities.length, 20); i++) {
        const sim = similarities[i];
        const stars = '⭐'.repeat(Math.min(Math.ceil(sim.score / 5), 5));
        
        report += `
### ${i + 1}. [[${sim.file.basename}]]

**Score**: ${sim.score} ${stars}  
**Type**: ${sim.type}  
**Reasons**: ${sim.reasons.join(' • ')}  
**Tags**: ${sim.tags.slice(0, 5).join(', ')}

`;
    }
    
    report += `
---

## 💡 Suggestions for Linking

### High Priority (Score > 15)
${similarities.filter(s => s.score > 15).map(s => 
    `- [[${s.file.basename}]] - Score: ${s.score}`
).join('\n') || '- None'}

### Medium Priority (Score 10-15)
${similarities.filter(s => s.score >= 10 && s.score <= 15).map(s => 
    `- [[${s.file.basename}]] - Score: ${s.score}`
).join('\n') || '- None'}

### Consider Linking (Score 5-9)
${similarities.filter(s => s.score >= 5 && s.score < 10).map(s => 
    `- [[${s.file.basename}]] - Score: ${s.score}`
).join('\n') || '- None'}

---

## 🏷️ Tag Analysis

### Most Common Tags in Related Notes
${getMostCommonTags(similarities)}

---

## 📊 Statistics

- **Total notes analyzed**: ${similarities.length}
- **High similarity (>15)**: ${similarities.filter(s => s.score > 15).length}
- **Medium similarity (10-15)**: ${similarities.filter(s => s.score >= 10 && s.score <= 15).length}
- **Low similarity (5-9)**: ${similarities.filter(s => s.score >= 5 && s.score < 10).length}

---

*This report was automatically generated. Review and add links as appropriate.*
`;
    
    return report;
}

function getMostCommonTags(similarities) {
    const tagCount = {};
    
    for (let sim of similarities) {
        for (let tag of sim.tags) {
            tagCount[tag] = (tagCount[tag] || 0) + 1;
        }
    }
    
    const sortedTags = Object.entries(tagCount)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 10);
    
    if (sortedTags.length === 0) return '- None';
    
    return sortedTags.map(([tag, count]) => `- \`${tag}\` (${count} notes)`).join('\n');
}

async function createFolderIfNotExists(app, path) {
    const folder = app.vault.getAbstractFileByPath(path);
    if (!folder) {
        await app.vault.createFolder(path);
    }
}

module.exports = find_related_notes;