/**
 * weekly-review.js
 * Templater script for generating weekly review reports
 * 
 * Generates a comprehensive weekly review including:
 * - Completed tasks
 * - Project progress
 * - Meetings attended
 * - Notes created
 * - Goals review
 * 
 * Usage: Run at end of week to generate review
 */

async function weekly_review(tp) {
    const { app } = tp;
    const moment = window.moment;
    
    // Calculate week dates
    const now = moment();
    const weekStart = now.clone().startOf('week');
    const weekEnd = now.clone().endOf('week');
    const weekNumber = now.format("WW");
    const year = now.format("YYYY");
    
    const weekLabel = `${year}-W${weekNumber}`;
    const weekTitle = `Week ${weekNumber} Review - ${weekStart.format("MMM DD")} to ${weekEnd.format("MMM DD, YYYY")}`;
    
    // Prompt for location
    const reviewFolder = "Reviews/Weekly";
    await createFolderIfNotExists(app, reviewFolder);
    
    // Generate review content
    const content = await generateReviewContent(app, weekStart, weekEnd, weekLabel, weekTitle);
    
    // Create the file
    const fileName = `${reviewFolder}/${weekLabel}.md`;
    
    try {
        const existingFile = app.vault.getAbstractFileByPath(fileName);
        if (existingFile) {
            const overwrite = await tp.system.prompt("File exists. Overwrite? (yes/no)");
            if (overwrite !== "yes") {
                new Notice("Weekly review cancelled");
                return;
            }
            await app.vault.delete(existingFile);
        }
        
        await app.vault.create(fileName, content);
        
        new Notice(`✅ Weekly review created: ${weekLabel}`);
        
        // Open the file
        const file = app.vault.getAbstractFileByPath(fileName);
        if (file) {
            await app.workspace.getLeaf().openFile(file);
        }
        
        return `Weekly review created: ${fileName}`;
        
    } catch (error) {
        new Notice(`❌ Error creating review: ${error.message}`);
        console.error("Weekly review error:", error);
        return `Error: ${error.message}`;
    }
}

async function generateReviewContent(app, weekStart, weekEnd, weekLabel, weekTitle) {
    const moment = window.moment;
    
    // Get all daily notes for the week
    const dailyNotes = await getDailyNotesForWeek(app, weekStart, weekEnd);
    
    // Get tasks completed this week
    const completedTasks = await getCompletedTasksForWeek(app, weekStart, weekEnd);
    
    // Get meetings this week
    const meetings = await getMeetingsForWeek(app, weekStart, weekEnd);
    
    // Get project updates
    const projectUpdates = await getProjectUpdates(app, weekStart, weekEnd);
    
    // Build content
    const content = `---
type: weekly-review
week: ${weekLabel}
week-start: ${weekStart.format("YYYY-MM-DD")}
week-end: ${weekEnd.format("YYYY-MM-DD")}
created: ${moment().format("YYYY-MM-DD HH:mm")}
tags:
  - review
  - weekly
  - ${moment().format("YYYY")}
---

# 📊 ${weekTitle}

## 🎯 Week Overview

### Week at a Glance
- **Week Number**: ${weekLabel}
- **Period**: ${weekStart.format("MMMM DD")} - ${weekEnd.format("MMMM DD, YYYY")}
- **Days Logged**: ${dailyNotes.length}/7
- **Tasks Completed**: ${completedTasks.length}
- **Meetings**: ${meetings.length}

### Overall Rating
**Rating**: ⭐⭐⭐⭐⭐ (X/5)

---

## ✅ Accomplishments

### Top Wins
1. 
2. 
3. 

### Tasks Completed (${completedTasks.length})

${completedTasks.length > 0 ? completedTasks.map(task => `- ${task}`).join('\n') : '- No tasks marked as completed this week'}

### Milestones Reached
- 

---

## 📊 Projects Update

${projectUpdates.length > 0 ? projectUpdates.map(project => `
### ${project.name}
- **Status**: ${project.status}
- **Progress**: ${project.progress}%
- **This Week**: 
- **Next Week**: 
`).join('\n') : '### No active projects tracked this week'}

---

## 🤝 Meetings & Collaboration (${meetings.length})

${meetings.length > 0 ? meetings.map(meeting => `
### ${meeting.title}
- **Date**: ${meeting.date}
- **Participants**: ${meeting.attendees}
- **Key Outcomes**: 
`).join('\n') : '- No meetings recorded this week'}

---

## 📚 Learning & Growth

### New Skills/Knowledge
- 

### Books/Articles Read
- 

### Key Insights
1. 
2. 
3. 

---

## 💭 Reflections

### What Went Well
1. 
2. 
3. 

### What Didn't Go Well
1. 
2. 
3. 

### What I Learned
- 

---

## 🚧 Challenges & Obstacles

### Blockers This Week
- 

### How I Addressed Them
- 

### Still Pending
- 

---

## 📈 Metrics & Tracking

### Time Distribution
- **Deep Work**: X hours
- **Meetings**: X hours
- **Admin**: X hours
- **Learning**: X hours

### Energy Levels
- **Average Energy**: ⭐⭐⭐⭐⭐
- **Best Day**: 
- **Worst Day**: 

### Habits Tracking
- **Exercise**: X/7 days
- **Meditation**: X/7 days
- **Reading**: X/7 days
- **Early Wake**: X/7 days

---

## 🎯 Goals Review

### Weekly Goals
- [ ] Goal 1 - Status: 
- [ ] Goal 2 - Status: 
- [ ] Goal 3 - Status: 

### Monthly Goals Progress
- Goal 1: XX% complete
- Goal 2: XX% complete

### Quarterly Goals Progress
- Goal 1: XX% complete
- Goal 2: XX% complete

---

## 📅 Daily Logs

${dailyNotes.length > 0 ? dailyNotes.map(note => `
### ${note.day} - ${note.date}
- **Mood**: ${note.mood || 'Not recorded'}
- **Energy**: ${note.energy || 'Not recorded'}
- **Highlights**: 
- **Link**: [[${note.filename}]]
`).join('\n') : '### No daily notes found for this week'}

---

## 🔄 Areas of Life Review

### 🏢 Work/Career
**Rating**: ⭐⭐⭐⭐⭐
- Wins: 
- Challenges: 
- Focus next week: 

### 💰 Finances
**Rating**: ⭐⭐⭐⭐⭐
- Progress: 
- Adjustments needed: 

### 💪 Health & Fitness
**Rating**: ⭐⭐⭐⭐⭐
- Exercise: 
- Nutrition: 
- Sleep quality: 

### 🧠 Learning & Growth
**Rating**: ⭐⭐⭐⭐⭐
- What I learned: 
- Skills developed: 

### 👥 Relationships
**Rating**: ⭐⭐⭐⭐⭐
- Quality time: 
- Connections made: 

### 🎨 Creativity & Hobbies
**Rating**: ⭐⭐⭐⭐⭐
- Projects: 
- Creative output: 

---

## 🎯 Next Week Planning

### Week ${parseInt(weekLabel.split('-W')[1]) + 1} Goals
1. 
2. 
3. 

### Key Priorities
- **Priority 1**: 
- **Priority 2**: 
- **Priority 3**: 

### Things to Prepare
- [ ] 
- [ ] 
- [ ] 

### Meetings Scheduled
- 

### Deadlines
- 

---

## 💡 Ideas & Notes

### New Ideas This Week
- 

### Things to Remember
- 

### Follow-up Items
- [ ] 
- [ ] 

---

## 🙏 Gratitude

1. 
2. 
3. 

---

## 📊 Week Statistics

\`\`\`dataview
TABLE WITHOUT ID
  file.link as "Daily Note",
  mood as "Mood",
  energy as "Energy",
  length(file.tasks) as "Tasks"
FROM "Daily Notes"
WHERE date >= date("${weekStart.format("YYYY-MM-DD")}") 
  AND date <= date("${weekEnd.format("YYYY-MM-DD")}")
SORT date ASC
\`\`\`

---

## 🔗 Related

- **Previous Week**: [[${moment().subtract(1, 'week').format("YYYY-[W]WW")}|Week ${parseInt(weekLabel.split('-W')[1]) - 1}]]
- **Next Week**: [[${moment().add(1, 'week').format("YYYY-[W]WW")}|Week ${parseInt(weekLabel.split('-W')[1]) + 1}]]
- **Monthly Review**: [[${moment().format("YYYY-MM")}|${moment().format("MMMM YYYY")}]]

---

**Created**: ${moment().format("YYYY-MM-DD HH:mm")}  
**Template**: weekly-review.js
`;
    
    return content;
}

async function getDailyNotesForWeek(app, weekStart, weekEnd) {
    const dailyNotes = [];
    const files = app.vault.getMarkdownFiles();
    
    for (let file of files) {
        if (file.path.includes("Daily Notes")) {
            const cache = app.metadataCache.getFileCache(file);
            if (cache && cache.frontmatter && cache.frontmatter.date) {
                const noteDate = window.moment(cache.frontmatter.date);
                if (noteDate.isBetween(weekStart, weekEnd, 'day', '[]')) {
                    dailyNotes.push({
                        date: cache.frontmatter.date,
                        day: noteDate.format("dddd"),
                        filename: file.basename,
                        mood: cache.frontmatter.mood || '',
                        energy: cache.frontmatter.energy || ''
                    });
                }
            }
        }
    }
    
    return dailyNotes.sort((a, b) => a.date.localeCompare(b.date));
}

async function getCompletedTasksForWeek(app, weekStart, weekEnd) {
    // This is a simplified version - real implementation would parse tasks
    const tasks = [];
    const files = app.vault.getMarkdownFiles();
    
    for (let file of files) {
        const cache = app.metadataCache.getFileCache(file);
        if (cache && cache.frontmatter && cache.frontmatter.type === 'task') {
            if (cache.frontmatter['completed-date']) {
                const completedDate = window.moment(cache.frontmatter['completed-date']);
                if (completedDate.isBetween(weekStart, weekEnd, 'day', '[]')) {
                    tasks.push(`[[${file.basename}]] - ${cache.frontmatter.title || file.basename}`);
                }
            }
        }
    }
    
    return tasks;
}

async function getMeetingsForWeek(app, weekStart, weekEnd) {
    const meetings = [];
    const files = app.vault.getMarkdownFiles();
    
    for (let file of files) {
        const cache = app.metadataCache.getFileCache(file);
        if (cache && cache.frontmatter && cache.frontmatter.type === 'meeting') {
            const meetingDate = window.moment(cache.frontmatter.date);
            if (meetingDate.isBetween(weekStart, weekEnd, 'day', '[]')) {
                meetings.push({
                    title: cache.frontmatter.title || file.basename,
                    date: cache.frontmatter.date,
                    attendees: cache.frontmatter.attendees ? cache.frontmatter.attendees.join(', ') : 'N/A'
                });
            }
        }
    }
    
    return meetings.sort((a, b) => a.date.localeCompare(b.date));
}

async function getProjectUpdates(app, weekStart, weekEnd) {
    const projects = [];
    const files = app.vault.getMarkdownFiles();
    
    for (let file of files) {
        const cache = app.metadataCache.getFileCache(file);
        if (cache && cache.frontmatter && cache.frontmatter.type === 'project') {
            if (cache.frontmatter.status === 'active' || cache.frontmatter.status === 'planning') {
                projects.push({
                    name: cache.frontmatter.title || file.basename,
                    status: cache.frontmatter.status || 'unknown',
                    progress: cache.frontmatter.progress || 0
                });
            }
        }
    }
    
    return projects;
}

async function createFolderIfNotExists(app, path) {
    const folder = app.vault.getAbstractFileByPath(path);
    if (!folder) {
        await app.vault.createFolder(path);
    }
}

module.exports = weekly_review;