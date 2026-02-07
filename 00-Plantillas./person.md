---
type: person
name: <% tp.file.cursor(1) %>
email: ""
phone: ""
company: ""
role: ""
location: ""
linkedin: ""
twitter: ""
website: ""
tags:
  - people
  - contact
category: professional
relationship: colleague
importance: medium
last-contact: <% tp.date.now("YYYY-MM-DD") %>
next-contact: ""
birthday: ""
interests: []
projects: []
---

# 👤 <% tp.frontmatter.name %>

> Quick context about this person

---

## 📇 Contact Information

| Field | Details |
|-------|---------|
| **Email** | `= this.email` |
| **Phone** | `= this.phone` |
| **Company** | `= this.company` |
| **Role** | `= this.role` |
| **Location** | `= this.location` |

### Social & Professional
- **LinkedIn**: `= this.linkedin`
- **Twitter**: `= this.twitter`
- **Website**: `= this.website`

---

## 🤝 Relationship

**Category**: `= this.category`  
**Relationship Type**: `= this.relationship`  
**Importance**: `= this.importance`

### How We Met
- **When**: 
- **Where**: 
- **Context**: 

### Connection Strength
- [ ] Close friend
- [ ] Good friend
- [ ] Colleague
- [ ] Acquaintance
- [ ] Professional contact
- [ ] Mentor/Mentee

---

## 💼 Professional Context

### Current Role


### Career Background


### Expertise & Skills
- 
- 
- 

### Can Help With
- 
- 
- 

### Looking For
- 
- 

---

## 🎯 Interests & Hobbies

### Professional Interests
- 

### Personal Interests
- 

### Topics We Discuss
- 
- 
- 

---

## 📅 Interaction History

### Recent Interactions
```dataview
TABLE date, type, summary
FROM "Meetings" OR "Notes"
WHERE contains(attendees, this.file.name) OR contains(people, this.file.name)
SORT date DESC
LIMIT 10
```

### Last Contact
**Date**: `= this.last-contact`  
**Context**: 

### Next Planned Contact
**Date**: `= this.next-contact`  
**Purpose**: 

---

## 💬 Conversation Log

### <% tp.date.now("YYYY-MM-DD") %> - <% tp.file.cursor(2) %>
**Medium**: [Call/Email/Meeting/Coffee/etc]




---

### [Date] - [Topic]
**Medium**: 




---

## 📋 Notes & Context

### Important Things to Remember
- 
- 
- 

### Topics to Discuss Next Time
- [ ] 
- [ ] 
- [ ] 

### Things They Care About
- **Family**: 
- **Career**: 
- **Projects**: 
- **Challenges**: 

---

## 🎁 Gifts & Occasions

### Birthday
**Date**: `= this.birthday`  
**Ideas**: 

### Gift History
| Date | Occasion | Gift | Notes |
|------|----------|------|-------|
| | | | |

---

## 🤲 How I Can Help

### Value I Can Provide
- 
- 
- 

### Introductions I Can Make
- 
- 

### Resources I Can Share
- 
- 

---

## 🙏 How They Can Help Me

### Expertise They Have
- 

### Connections They Have
- 

### Advice They Can Give
- 

---

## 📊 Projects & Collaborations

### Current Projects Together
```dataview
TABLE status, priority, role
FROM "Projects"
WHERE contains(stakeholders, this.file.name)
SORT priority DESC
```

### Past Collaborations
- **[Project Name]** - [Year] - [Outcome]
- 

### Future Opportunities
- 

---

## 📚 Resources Shared

### From Them to Me
- [[]] - [Description]
- 

### From Me to Them
- [[]] - [Description]
- 

### Mutual Interests
- 

---

## 🎓 Learning & Growth

### What I've Learned from Them
- 
- 

### Advice They've Given
> 

### Their Growth Areas
- 

---

## 🌐 Network

### Mutual Connections
```dataview
LIST
FROM "People"
WHERE file.name != this.file.name
  AND (contains(company, this.company) OR contains(tags, "network"))
```

### People They Know
- [[Person 1]] - [Relationship]
- [[Person 2]] - [Relationship]

### Introductions Made
- **[Date]**: Introduced [[Person A]] to [[Person B]]
- 

---

## 📧 Communication Preferences

### Preferred Method
- [ ] Email
- [ ] Phone
- [ ] Text/WhatsApp
- [ ] LinkedIn
- [ ] In-person

### Response Time
- Usually responds within: 

### Best Time to Contact
- 

### Communication Style
- 

---

## 🎯 Action Items

### Immediate
- [ ] 
- [ ] 

### Short-term
- [ ] 
- [ ] 

### Long-term
- [ ] 
- [ ] 

---

## 📈 Relationship Goals

### What I Want from This Relationship
- 

### How to Strengthen Connection
- 
- 
- 

### Frequency of Contact
**Ideal**: 
**Current**: 

---

## 🗒️ Quick Notes




---

## 🏷️ Tags & Categories

**Tags**: `= this.tags`  
**Category**: `= this.category`  
**Projects**: `= this.projects`

---

## 📎 Attachments

- 

---

## 🔗 Related

### Related People
```dataview
TABLE company, role, relationship
FROM "People"
WHERE file.name != this.file.name
  AND (company = this.company OR contains(interests, this.interests))
LIMIT 5
```

### Related Meetings
```dataview
TABLE date, title
FROM "Meetings"
WHERE contains(attendees, this.file.name)
SORT date DESC
LIMIT 5
```

---

## 🏁 Summary

### In One Sentence


### Key Characteristics
- 
- 
- 

---

**Created**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Last Updated**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Template**: person.md