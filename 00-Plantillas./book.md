---
type: book
title: <% tp.file.cursor(1) %>
author: <% tp.file.cursor(2) %>
subtitle: ""
isbn: ""
publisher: ""
published: ""
pages: 0
format: physical
language: en
genre: []
tags:
  - books
  - reading
status: to-read
rating: 0
date-started: ""
date-finished: ""
recommended-by: ""
purchase-link: ""
goodreads: ""
---

# 📚 <% tp.frontmatter.title %>

**By**: <% tp.frontmatter.author %>

> One-line description or hook

---

## 📖 Book Information

| Field | Details |
|-------|---------|
| **Title** | `= this.title` |
| **Author** | `= this.author` |
| **Published** | `= this.published` |
| **Pages** | `= this.pages` |
| **Format** | `= this.format` |
| **Status** | `= this.status` |
| **Rating** | `= this.rating`/5 ⭐ |

### Reading Timeline
- **Started**: `= this.date-started`
- **Finished**: `= this.date-finished`
- **Reading Time**: 

---

## 🎯 Why I'm Reading This

### Main Goal


### What I Hope to Learn
- 
- 
- 

### Recommended By
`= this.recommended-by`

### Context


---

## 📝 Summary

### One-Paragraph Summary


### Three Key Takeaways
1. 
2. 
3. 

### Central Thesis


---

## 📋 Chapter Notes

### Chapter 1: <% tp.file.cursor(3) %>
**Key Points**:
- 
- 

**Quotes**:
> 

**My Thoughts**:


**Action Items**:
- [ ] 

---

### Chapter 2: 
**Key Points**:
- 

**Quotes**:
> 

**My Thoughts**:


---

### Chapter 3: 
**Key Points**:
- 

**Quotes**:
> 

**My Thoughts**:


---

## 💡 Key Concepts & Ideas

### Concept 1: 
**Definition**:


**Application**:


**Related to**: [[]]

---

### Concept 2: 
**Definition**:


**Application**:


---

### Concept 3: 
**Definition**:


**Application**:


---

## 📑 Favorite Quotes

> "Quote 1"
> — Page X

> "Quote 2"
> — Page Y

> "Quote 3"
> — Page Z

---

## 🔍 Deep Dive

### Most Surprising Insights
- 
- 

### Controversial Points
- 
- 

### Questions Raised
- 
- 

### Disagreements
- 

---

## 🌟 Highlights & Annotations

### Section 1: [Chapter/Part Name]
**Page**: 

**Highlight**:
> 

**My Note**:


**Tags**: #

---

### Section 2:
**Page**: 

**Highlight**:
> 

**My Note**:


---

## 🔗 Connections

### Related Books
```dataview
TABLE author, rating, status
FROM "Books"
WHERE file.name != this.file.name
  AND (contains(genre, this.genre) OR author = this.author)
SORT rating DESC
```

### Related Notes
- [[]] - 
- [[]] - 

### Projects Influenced
- [[]] - 

### People to Discuss With
- [[]] - 

---

## 💭 Critical Analysis

### Strengths
- 
- 
- 

### Weaknesses
- 
- 

### Writing Style


### Target Audience


### Bias & Perspective


---

## 🎯 Actionable Takeaways

### Immediate Actions
- [ ] 
- [ ] 
- [ ] 

### Long-term Changes
- 
- 

### Habits to Develop
- 
- 

### Ideas to Explore Further
- 
- 

---

## 📊 Book Structure

### Part I: 
- Chapter 1: 
- Chapter 2: 
- Chapter 3: 

### Part II: 
- Chapter 4: 
- Chapter 5: 

### Part III: 
- Chapter 6: 
- Chapter 7: 

---

## 🎓 Learning Outcomes

### What I Learned
1. 
2. 
3. 

### Skills Developed
- 

### Mental Models Acquired
- 

### Paradigm Shifts
- 

---

## ⭐ My Review

### Overall Rating
**Rating**: ⭐⭐⭐⭐⭐ (`= this.rating`/5)

### Detailed Rating
- **Content**: ⭐⭐⭐⭐⭐
- **Writing**: ⭐⭐⭐⭐⭐
- **Originality**: ⭐⭐⭐⭐⭐
- **Practical Value**: ⭐⭐⭐⭐⭐
- **Enjoyment**: ⭐⭐⭐⭐⭐

### Review


### Would I Recommend?
**Yes/No** - To whom: 

### Would I Re-read?
**Yes/No** - When: 

---

## 👥 Discussions & Sharing

### Book Club Notes


### Conversations About This Book
- **With [[Person]]** on [Date]:
  - 

### Social Media Posts
- 

---

## 📚 Further Reading

### Recommended Next
1. [[Book]] by Author
2. [[Book]] by Author

### References & Sources
- 

### Author's Other Works
- 

---

## 🖼️ Visual Notes

### Concept Map


### Mindmap of Key Ideas


### Diagrams


---

## 🔖 Reading Progress

### Progress Log
- **10%** (<% tp.date.now("YYYY-MM-DD") %>): 
- **25%**: 
- **50%**: 
- **75%**: 
- **100%**: 

### Reading Pace
- Average pages per day: 
- Estimated completion: 

---

## 💼 Practical Applications

### In Work


### In Personal Life


### In Relationships


### In Learning


---

## 🎯 Post-Reading Plan

### Immediate (This Week)
- [ ] Write review
- [ ] Share key insights
- [ ] Create permanent notes

### Short-term (This Month)
- [ ] Apply concept X
- [ ] Discuss with [[Person]]
- [ ] Read related book

### Long-term
- [ ] 

---

## 📎 Resources

### Book Website
- 

### Author Website
- 

### Supporting Materials
- 

### Videos & Podcasts
- 

---

## 🏷️ Metadata

**Genre**: `= this.genre`  
**Language**: `= this.language`  
**ISBN**: `= this.isbn`  
**Goodreads**: `= this.goodreads`  
**Purchase**: `= this.purchase-link`

---

## 📊 Reading Statistics

```dataview
TABLE 
  author,
  pages,
  rating,
  date-finished as "Completed"
FROM "Books"
WHERE status = "completed"
SORT date-finished DESC
LIMIT 10
```

---

**Created**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Last Updated**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Template**: book.md