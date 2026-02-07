---
type: article
title: <% tp.file.cursor(1) %>
author: <% tp.file.cursor(2) %>
source: ""
url: ""
published: ""
accessed: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - article
  - resource
category: ""
topic: []
status: to-read
rating: 0
reading-time: ""
---

# 📄 <% tp.frontmatter.title %>

**Author**: <% tp.frontmatter.author %>  
**Source**: `= this.source`  
**URL**: `= this.url`  
**Published**: `= this.published`

> TL;DR: One-sentence summary

---

## 🎯 Context

### Why I'm Reading This


### Relevance to My Work/Interests


### How I Found It


---

## 📝 Summary

### Executive Summary (3-5 sentences)


### Key Points
1. 
2. 
3. 
4. 
5. 

---

## 💡 Main Arguments

### Argument 1


**Evidence**:
- 

**My Take**:


---

### Argument 2


**Evidence**:
- 

**My Take**:


---

## 📊 Data & Facts

### Key Statistics
- 
- 
- 

### Research Cited
- 

### Case Studies
- 

---

## 💬 Notable Quotes

> "Quote 1"

> "Quote 2"

> "Quote 3"

---

## 🔍 Critical Analysis

### Strengths
- 
- 

### Weaknesses
- 
- 

### Bias/Perspective


### Credibility Assessment
- [ ] Peer-reviewed
- [ ] Reputable source
- [ ] Citations provided
- [ ] Data verifiable
- [ ] Author expertise confirmed

---

## 🌟 Insights & Takeaways

### New Ideas
- 
- 

### Confirmed Beliefs
- 

### Challenged Assumptions
- 

### Surprises
- 

---

## 🔗 Connections

### Related Articles
```dataview
TABLE author, source, rating, status
FROM "Articles"
WHERE file.name != this.file.name
  AND (contains(topic, this.topic) OR contains(category, this.category))
SORT rating DESC
LIMIT 5
```

### Related Notes
- [[]] - 
- [[]] - 

### Related Projects
- [[]] - 

---

## 🎯 Action Items

### To Research Further
- [ ] 
- [ ] 

### To Apply
- [ ] 
- [ ] 

### To Share With
- [ ] [[Person]] - Why: 
- [ ] [[Person]] - Why: 

---

## 📚 References & Citations

### Sources Cited in Article
1. 
2. 
3. 

### Related Reading
- 
- 

---

## 🗒️ Detailed Notes

### Section 1: Introduction


### Section 2: Main Content


### Section 3: Conclusion


---

## ⭐ My Rating & Review

**Overall Rating**: ⭐⭐⭐⭐⭐ (`= this.rating`/5)

**Detailed Ratings**:
- **Content Quality**: ⭐⭐⭐⭐⭐
- **Originality**: ⭐⭐⭐⭐⭐
- **Practical Value**: ⭐⭐⭐⭐⭐
- **Readability**: ⭐⭐⭐⭐⭐

### Review


### Would I Recommend?
**Yes/No** - To whom: 

---

## 🎓 Learning Outcomes

### What I Learned


### Questions Raised


### Follow-up Topics


---

## 📎 Attachments

- 

---

**Created**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Last Updated**: <% tp.date.now("YYYY-MM-DD HH:mm") %>  
**Reading Time**: `= this.reading-time`  
**Template**: article.md