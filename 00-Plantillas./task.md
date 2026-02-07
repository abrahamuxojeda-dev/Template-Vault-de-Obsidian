---
type: task
title: <% tp.file.cursor(1) %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
status: todo
priority: medium
effort: medium
impact: medium
tags:
  - task
  - action
due-date: ""
start-date: ""
completed-date: ""
context: []
energy-level: medium
time-estimate: ""
project: ""
area: ""
assignee: ""
delegated-to: ""
---

# ✅ <% tp.frontmatter.title %>

> Brief description of what needs to be done

---

## 📊 Task Overview

| Field | Value |
|-------|-------|
| **Status** | `= this.status` |
| **Priority** | `= this.priority` |
| **Effort** | `= this.effort` |
| **Impact** | `= this.impact` |
| **Due Date** | `= this.due-date` |
| **Time Estimate** | `= this.time-estimate` |
| **Context** | `= this.context` |
| **Energy Level** | `= this.energy-level` |

---

## 🎯 Task Details

### What Needs to Be Done?


### Why Is This Important?


### Success Criteria
- [ ] 
- [ ] 
- [ ] 

### Definition of Done
- [ ] 
- [ ] 

---

## 📋 Subtasks

### Main Steps
- [ ] Step 1 - 
- [ ] Step 2 - 
- [ ] Step 3 - 
- [ ] Step 4 - 
- [ ] Step 5 - 

### Preparation Needed
- [ ] 
- [ ] 

### Follow-up Actions
- [ ] 
- [ ] 

---

## 🔗 Dependencies

### Blocked By
- [ ] [[Task]] - Reason: 
- [ ] 

### Blocking
- [ ] [[Task]] - How: 
- [ ] 

### Related Tasks
```dataview
TABLE status, priority, due-date as "Due"
FROM "Tasks"
WHERE file.name != this.file.name
  AND (project = this.project OR contains(tags, "task"))
SORT priority DESC, due-date ASC
LIMIT 5
```

---

## 🛠️ Resources Needed

### Tools & Systems
- 
- 

### Information/Documents
- [[]] - 
- 

### People to Consult
- [[Person]] - For: 
- 

### Prerequisites
- 

---

## 🗓️ Timeline

### Planned Start
**Date**: `= this.start-date`  
**Time Block**: 

### Due Date
**Date**: `= this.due-date`  
**Hard Deadline?**: Yes/No

### Time Allocation
- **Estimated Time**: `= this.time-estimate`
- **Actual Time**: 
- **Time Tracking**:
  - Session 1: [Date] - [Duration]
  - Session 2: [Date] - [Duration]

---

## 👤 Ownership

### Assignee
**Owner**: `= this.assignee`

### Delegation
**Delegated To**: `= this.delegated-to`  
**Instructions**: 
**Check-in Date**: 

---

## 📁 Context & Project

### Project
**Related Project**: [[`= this.project`]]

### Area of Life/Work
**Area**: `= this.area`

### Context Tags
`= this.context`

### When to Do This?
- [ ] `#context/home`
- [ ] `#context/work`
- [ ] `#context/computer`
- [ ] `#context/phone`
- [ ] `#context/errands`
- [ ] `#context/anywhere`

---

## 🧠 Planning & Strategy

### Approach


### Potential Obstacles
1. 
   - **Mitigation**: 
2. 
   - **Mitigation**: 

### Alternative Approaches
- **Plan A**: 
- **Plan B**: 
- **Plan C**: 

---

## 📝 Work Log

### <% tp.date.now("YYYY-MM-DD HH:mm") %>
**Session Duration**: 
**Progress Made**: 
**Challenges**: 
**Next Steps**: 

---

### [Date & Time]
**Session Duration**: 
**Progress Made**: 
**Challenges**: 
**Next Steps**: 

---

## 💡 Notes & Ideas

### Insights While Working


### Questions That Came Up
- 

### Things to Remember
- 

---

## ✨ Improvements & Learnings

### What Worked Well
- 

### What Didn't Work
- 

### What Would I Do Differently?
- 

### Skills Developed
- 

---

## 🎯 Outcome

### Final Result


### Success Evaluation
- [ ] Met success criteria
- [ ] Completed on time
- [ ] Within effort estimate
- [ ] Quality satisfactory

### Impact Achieved


---

## 🔄 Follow-up

### Next Actions
- [ ] 
- [ ] 

### Related Tasks to Create
- [ ] 
- [ ] 

### People to Inform
- [ ] [[Person]] - About: 
- [ ] 

---

## 📎 Attachments

- 

---

## 🏷️ Priority Matrix

**Priority**: `= this.priority`  
**Effort**: `= this.effort`  
**Impact**: `= this.impact`

### Eisenhower Matrix
- [ ] Urgent & Important (Do First)
- [ ] Not Urgent & Important (Schedule)
- [ ] Urgent & Not Important (Delegate)
- [ ] Not Urgent & Not Important (Eliminate)

---

## 📊 Tracking

### Status History
- **Todo** → **In Progress**: [Date]
- **In Progress** → **Completed**: [Date]

### Priority Changes
- Initial: `= this.priority`
- Current: 

---

## 🔗 Related Items

### Related Meetings
```dataview
TABLE date, title, attendees
FROM "Meetings"
WHERE contains(action-items, this.file.name)
SORT date DESC
LIMIT 3
```

### Related Projects
- [[`= this.project`]]

### Related People
- [[`= this.assignee`]]
- [[`= this.delegated-to`]]

---

## 💬 Comments & Discussion

### <% tp.date.now("YYYY-MM-DD") %>


---

### [Date]


---

## 📈 Analytics

### Effort vs. Impact
- **Effort**: `= this.effort`
- **Impact**: `= this.impact`
- **Ratio**: 

### Time Tracking
- **Estimated**: `= this.time-estimate`
- **Actual**: 
- **Variance**: 

---

## ✅ Completion Checklist

- [ ] All subtasks completed
- [ ] Success criteria met
- [ ] Follow-up actions created
- [ ] Stakeholders informed
- [ ] Documentation updated
- [ ] Lessons learned recorded

---

## 🗑️ Cancellation (if applicable)

### Reason for Cancellation


### Learnings


### Can Be Salvaged?


---

## 🏷️ Metadata

**Created**: `= this.created`  
**Updated**: `= this.updated`  
**Status**: `= this.status`  
**Tags**: `= this.tags`

---

**Template**: task.md