---
type: daily-note
date: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
week: <% tp.date.now("YYYY-[W]WW") %>
tags:
  - daily
  - journal/<% tp.date.now("YYYY") %>/<% tp.date.now("MM") %>
weather: ""
mood: ""
energy: ""
---

# <% tp.date.now("dddd, MMMM DD, YYYY") %>

← [[<% tp.date.now("YYYY-MM-DD", -1) %>|Yesterday]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>|Tomorrow]] →

## 🎯 Daily Intention

> What's the ONE thing I can do today that will make everything else easier?

<% tp.file.cursor(1) %>

---

## ✅ Today's Priorities

- [ ] **Priority 1**: 
- [ ] **Priority 2**: 
- [ ] **Priority 3**: 

---

## 📝 Log

### Morning (06:00 - 12:00)


### Afternoon (12:00 - 18:00)


### Evening (18:00 - 00:00)


---

## 💭 Notes & Ideas

- 

---

## 🙏 Gratitude

1. 
2. 
3. 

---

## 📊 Metrics

- **Sleep**: ⭐⭐⭐⭐⭐
- **Exercise**: ⭐⭐⭐⭐⭐
- **Nutrition**: ⭐⭐⭐⭐⭐
- **Focus**: ⭐⭐⭐⭐⭐
- **Social**: ⭐⭐⭐⭐⭐

**Overall Day Rating**: ⭐⭐⭐⭐⭐

---

## 🔗 Related

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  tags as "Tags"
FROM ""
WHERE contains(file.name, "<% tp.date.now("YYYY-MM-DD") %>")
  OR contains(string(file.cday), "<% tp.date.now("YYYY-MM-DD") %>")
SORT file.mtime DESC
LIMIT 10
```

---

## 📎 Connections

<!-- Links to related notes, projects, or people -->

---

## 🌙 Evening Reflection

### What went well?


### What could improve?


### Tomorrow's focus?


---

## 📅 Weekly Context

**Week**: [[<% tp.date.now("YYYY-[W]WW") %>|Week <% tp.date.now("WW") %>]]  
**Month**: [[<% tp.date.now("YYYY-MM") %>|<% tp.date.now("MMMM YYYY") %>]]  
**Quarter**: [[<% tp.date.now("YYYY-[Q]Q") %>|Q<% tp.date.now("Q") %> <% tp.date.now("YYYY") %>]]

---

*Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>*