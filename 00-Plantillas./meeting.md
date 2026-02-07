---
type: meeting
title: <% tp.file.cursor(1) %>
date: <% tp.date.now("YYYY-MM-DD") %>
time: <% tp.date.now("HH:mm") %>
duration: 60
location: ""
meeting-type: regular
status: scheduled
tags:
  - meeting
  - meeting/<% tp.date.now("YYYY") %>
attendees: []
organizer: ""
related-project: ""
next-meeting: ""
---

# 🤝 <% tp.frontmatter.title %>

**📅 Date**: <% tp.date.now("dddd, MMMM DD, YYYY") %>  
**⏰ Time**: <% tp.date.now("HH:mm") %> - <% tp.date.now("HH:mm", "60 minutes") %>  
**📍 Location**: <% tp.file.cursor(2) %>  
**👤 Organizer**: <% tp.file.cursor(3) %>

---

## 👥 Attendees

### Present
- [ ] 
- [ ] 
- [ ] 

### Absent
- [ ] 
- [ ] 

### Optional
- [ ] 

---

## 📋 Agenda

### 1. Opening (5 min)
- Quick round of updates
- Review agenda

### 2. Main Topics

#### Topic 1: <% tp.file.cursor(4) %> (20 min)
**Owner**: 
**Goal**: 

**Discussion Points**:
- 
- 
- 

**Notes**:


#### Topic 2:  (15 min)
**Owner**: 
**Goal**: 

**Discussion Points**:
- 
- 

**Notes**:


#### Topic 3:  (15 min)
**Owner**: 
**Goal**: 

**Discussion Points**:
- 

**Notes**:


### 3. Q&A (5 min)


### 4. Wrap-up (5 min)
- Review action items
- Schedule next meeting

---

## 📝 Meeting Notes

### Key Discussion Points


### Important Quotes
> 


### Brainstorming Ideas
- 
- 
- 

---

## ✅ Action Items

```dataview
TASK
WHERE contains(file.name, this.file.name) OR contains(meeting, this.file.name)
WHERE !completed
SORT priority DESC
```

### Priority Action Items
- [ ] **@person** - Action item 1 - 📅 Due: 
- [ ] **@person** - Action item 2 - 📅 Due: 
- [ ] **@person** - Action item 3 - 📅 Due: 

### Follow-up Required
- [ ] 
- [ ] 

---

## 🎯 Decisions Made

| Decision | Rationale | Owner | Impact |
|----------|-----------|-------|--------|
| | | | High/Med/Low |
| | | | High/Med/Low |

---

## 🚧 Blockers & Issues

| Issue | Owner | Status | Resolution |
|-------|-------|--------|------------|
| | | 🔴 | |
| | | 🟡 | |

---

## 📊 Project Updates

### Project Status Overview


### Metrics Review


### Upcoming Milestones
- 

---

## 💡 Ideas & Suggestions

### New Ideas
- 

### Parking Lot (Future Discussion)
- 
- 

---

## 📎 Resources Mentioned

### Documents
- [[]] - 
- [[]] - 

### Tools & Systems
- 

### External Links
- []() - 

---

## 🔄 Follow-up Items

### Before Next Meeting
- [ ] 
- [ ] 
- [ ] 

### For Future Meetings
- 

---

## 📅 Next Meeting

**Date**: 
**Time**: 
**Location**: 
**Agenda Preview**:
- 
- 

---

## 📧 Meeting Summary (Email Draft)

**Subject**: Meeting Summary - <% tp.frontmatter.title %> - <% tp.date.now("MMM DD") %>

**Hi Team,**

Thank you for attending today's meeting. Here's a quick summary:

**Key Decisions:**
- 

**Action Items:**
- @person - Task - Due: Date
- @person - Task - Due: Date

**Next Meeting:** Date & Time

Please reach out if you have any questions.

Best regards,

---

## 🔗 Related

### Related Meetings
```dataview
TABLE date, attendees, status
FROM "Meetings"
WHERE file.name != this.file.name
  AND (contains(related-project, this.related-project) OR contains(tags, "meeting"))
SORT date DESC
LIMIT 5
```

### Related Projects
- [[<% tp.frontmatter.related-project %>]]

### Related People
```dataview
LIST
FROM "People"
WHERE contains(this.attendees, file.name)
```

---

## 📈 Meeting Effectiveness

**Rating**: ⭐⭐⭐⭐⭐

### What Went Well
- 

### What Could Improve
- 

### Action for Next Time
- 

---

## 🏷️ Metadata

**Created**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Meeting Type**: `= this.meeting-type`  
**Duration**: `= this.duration` minutes  
**Recording**: 
**Transcript**: 

---

## Attendance Record

```dataview
TABLE 
  attendees,
  duration as "Duration (min)",
  status
FROM "Meetings"
WHERE contains(file.folder, "Meetings")
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

---

*Template: meeting.md*