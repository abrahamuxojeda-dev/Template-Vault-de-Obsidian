/**
 * create-project.js
 * Templater script for creating complete project structures
 * 
 * Creates:
 * - Main project file
 * - Project folder with subfolders
 * - Initial task list
 * - Meeting notes folder
 * 
 * Usage: Execute from Templater command palette
 */

async function create_project(tp) {
    const { app } = tp;
    
    // Get project name from user
    const projectName = await tp.system.prompt("Project Name");
    if (!projectName) {
        new Notice("Project creation cancelled");
        return;
    }
    
    const projectSlug = projectName.toLowerCase().replace(/\s+/g, '-');
    const projectArea = await tp.system.suggester(
        ["Work", "Personal", "Learning", "Side Project", "Client Work", "Other"],
        ["work", "personal", "learning", "side-project", "client", "other"],
        false,
        "Select project area"
    );
    
    const projectPriority = await tp.system.suggester(
        ["🔴 High", "🟡 Medium", "🟢 Low"],
        ["high", "medium", "low"],
        false,
        "Select priority"
    );
    
    // Create project structure
    const basePath = `Projects/${projectSlug}`;
    
    try {
        // Create folders
        await createFolderIfNotExists(app, basePath);
        await createFolderIfNotExists(app, `${basePath}/Tasks`);
        await createFolderIfNotExists(app, `${basePath}/Meetings`);
        await createFolderIfNotExists(app, `${basePath}/Documents`);
        await createFolderIfNotExists(app, `${basePath}/Resources`);
        
        // Create main project file
        const projectContent = `---
type: project
title: ${projectName}
status: planning
priority: ${projectPriority}
area: ${projectArea}
created: ${tp.date.now("YYYY-MM-DD")}
updated: ${tp.date.now("YYYY-MM-DD")}
start-date: ""
deadline: ""
progress: 0
tags:
  - project
  - project/active
  - area/${projectArea}
---

# 📋 ${projectName}

## 🎯 Objective

[Define the main objective]

## 📝 Description

[Describe the project]

## ✅ Success Criteria

- [ ] 
- [ ] 
- [ ] 

## 📅 Milestones

- [ ] **M1**: Milestone 1 - Due: 
- [ ] **M2**: Milestone 2 - Due: 
- [ ] **M3**: Milestone 3 - Due: 

## 📋 Tasks

\`\`\`dataview
TASK
WHERE contains(file.path, "${basePath}")
WHERE !completed
SORT priority DESC
\`\`\`

## 📁 Project Files

- [[${basePath}/Tasks/Index|Tasks]]
- [[${basePath}/Meetings/Index|Meetings]]
- [[${basePath}/Documents/Index|Documents]]
- [[${basePath}/Resources/Index|Resources]]

## 🔗 Related

`;
        
        await app.vault.create(`${basePath}/${projectSlug}.md`, projectContent);
        
        // Create task index
        const taskIndexContent = `# Tasks - ${projectName}

## 🔥 High Priority
\`\`\`dataview
TASK
WHERE contains(file.path, "${basePath}/Tasks") AND priority = "high"
WHERE !completed
\`\`\`

## 📌 Medium Priority
\`\`\`dataview
TASK
WHERE contains(file.path, "${basePath}/Tasks") AND priority = "medium"
WHERE !completed
\`\`\`

## 📝 Low Priority
\`\`\`dataview
TASK
WHERE contains(file.path, "${basePath}/Tasks") AND priority = "low"
WHERE !completed
\`\`\`

## ✔️ Completed
\`\`\`dataview
TASK
WHERE contains(file.path, "${basePath}/Tasks")
WHERE completed
SORT completion DESC
LIMIT 20
\`\`\`
`;
        await app.vault.create(`${basePath}/Tasks/Index.md`, taskIndexContent);
        
        // Create meetings index
        const meetingsIndexContent = `# Meetings - ${projectName}

\`\`\`dataview
TABLE date, attendees, status
FROM "${basePath}/Meetings"
WHERE type = "meeting"
SORT date DESC
\`\`\`
`;
        await app.vault.create(`${basePath}/Meetings/Index.md`, meetingsIndexContent);
        
        // Create documents index
        const docsIndexContent = `# Documents - ${projectName}

\`\`\`dataview
TABLE file.ctime as Created, file.mtime as Modified, tags
FROM "${basePath}/Documents"
SORT file.mtime DESC
\`\`\`
`;
        await app.vault.create(`${basePath}/Documents/Index.md`, docsIndexContent);
        
        // Create resources index
        const resourcesIndexContent = `# Resources - ${projectName}

## 📚 References

## 🔗 Links

## 📎 Files

`;
        await app.vault.create(`${basePath}/Resources/Index.md`, resourcesIndexContent);
        
        // Create first task
        const firstTaskContent = `---
type: task
title: Setup ${projectName}
status: todo
priority: high
project: ${projectSlug}
created: ${tp.date.now("YYYY-MM-DD")}
tags:
  - task
  - project/${projectSlug}
---

# ✅ Setup ${projectName}

## 📝 Description

Initial setup tasks for the project.

## 📋 Subtasks

- [ ] Define project scope
- [ ] Identify stakeholders
- [ ] Set initial milestones
- [ ] Create task list
- [ ] Schedule kickoff meeting
`;
        await app.vault.create(`${basePath}/Tasks/setup-project.md`, firstTaskContent);
        
        new Notice(`✅ Project "${projectName}" created successfully!`);
        
        // Open the main project file
        const projectFile = app.vault.getAbstractFileByPath(`${basePath}/${projectSlug}.md`);
        if (projectFile) {
            await app.workspace.getLeaf().openFile(projectFile);
        }
        
        return `Project "${projectName}" created at ${basePath}`;
        
    } catch (error) {
        new Notice(`❌ Error creating project: ${error.message}`);
        console.error("Project creation error:", error);
        return `Error: ${error.message}`;
    }
}

async function createFolderIfNotExists(app, path) {
    const folder = app.vault.getAbstractFileByPath(path);
    if (!folder) {
        await app.vault.createFolder(path);
    }
}

module.exports = create_project;