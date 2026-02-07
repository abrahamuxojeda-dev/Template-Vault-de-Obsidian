# 📖 Usage Examples

Esta guía muestra ejemplos prácticos de cómo usar el sistema de Obsidian.

## 🗓️ Daily Notes Workflow

### Crear Nota Diaria
```markdown
1. Click en el ícono de calendario, o
2. Ctrl/Cmd + P → "Open today's daily note", o
3. Click en la fecha en el plugin Calendar
```

### Ejemplo de Nota Diaria Completada
```markdown
---
type: daily-note
date: 2026-02-02
day: Monday
tags:
  - daily
  - journal/2026/02
mood: "energetic"
energy: "high"
---

# Monday, February 02, 2026

## 🎯 Daily Intention
Launch the new marketing campaign

## ✅ Today's Priorities
- [x] Complete campaign assets
- [x] Review with team
- [ ] Schedule launch

## 📝 Log

### Morning
- 8:00 AM: Team standup
- 9:00 AM: Deep work on campaign
- 11:00 AM: Client call

### Afternoon
- 2:00 PM: Campaign review
- 4:00 PM: Email responses

## 💭 Notes & Ideas
- New idea for Q2 content strategy
- Consider automation for social posts

## 🙏 Gratitude
1. Great collaboration from the team
2. Productive deep work session
3. Positive client feedback

**Overall Day Rating**: ⭐⭐⭐⭐⭐
```

## 📋 Project Management

### Crear Nuevo Proyecto
```markdown
1. Ctrl/Cmd + P → "Templater: Create new note from template"
2. Selecciona "project.md"
3. Nombra el proyecto
4. Completa los campos
```

### Ejemplo de Proyecto
```markdown
---
type: project
title: Website Redesign
status: active
priority: high
area: work
created: 2026-02-02
deadline: 2026-03-15
progress: 35
tags:
  - project
  - project/active
  - area/work
---

# 📋 Website Redesign

## 🎯 Objective
Modernize company website to improve conversion rate by 25%

## ✅ Success Criteria
- [x] New design approved
- [ ] Development complete
- [ ] SEO optimized
- [ ] Launch successful

## 📅 Milestones
- [x] **M1**: Design Phase - 2026-01-15 ✅
- [ ] **M2**: Development - 2026-02-28
- [ ] **M3**: Testing - 2026-03-10
- [ ] **M4**: Launch - 2026-03-15

## 📝 Recent Updates
- **2026-02-02**: Development 35% complete, on track
- **2026-01-28**: Design approved by stakeholders
```

## ✅ Task Management

### Crear Tarea Individual
```markdown
---
type: task
title: Implement user authentication
status: in-progress
priority: high
due-date: 2026-02-10
project: website-redesign
context: [work, computer]
---

# ✅ Implement user authentication

## 📋 Subtasks
- [x] Research OAuth providers
- [x] Choose implementation approach
- [ ] Implement login flow
- [ ] Add password reset
- [ ] Write tests

## 🔗 Dependencies
- Blocked by: [[Setup database schema]]
- Blocking: [[User dashboard]]
```

### Vista de Tareas con Dataview
```markdown
## 🔥 High Priority Tasks
```dataview
TASK
WHERE priority = "high" AND !completed
SORT due-date ASC
```

## 📊 Active Projects
```dataview
TABLE status, priority, progress as "Progress %", deadline
FROM "Projects"
WHERE status = "active"
SORT priority DESC, deadline ASC
```
```

## 🤝 Meeting Notes

### Preparar Reunión
```markdown
---
type: meeting
title: Q1 Planning Meeting
date: 2026-02-05
time: 14:00
attendees: [Alice, Bob, Carol]
---

# 🤝 Q1 Planning Meeting

## 📋 Agenda
1. Review Q4 results (15 min)
2. Set Q1 goals (20 min)
3. Resource allocation (15 min)
4. Q&A (10 min)

## ✅ Action Items
- [ ] @Alice - Prepare Q4 report by Friday
- [ ] @Bob - Draft Q1 budget proposal
- [ ] @Carol - Schedule follow-up meetings
```

## 💡 Idea Capture

### Captura Rápida
```markdown
---
type: idea
title: AI-powered content recommendation
created: 2026-02-02
status: captured
category: product
priority: medium
---

# 💡 AI-powered content recommendation

## 🎯 The Idea
Use ML to recommend personalized content to users based on their behavior

## 📊 Quick Assessment
- **Effort**: High (6 months)
- **Impact**: High (could increase engagement 40%)
- **Feasibility**: Medium (need ML expertise)

## 🔍 Next Steps
- [ ] Research similar implementations
- [ ] Talk to ML team
- [ ] Estimate costs
```

## 📚 Reading Notes

### Notas de Libro
```markdown
---
type: book
title: Atomic Habits
author: James Clear
status: reading
rating: 5
date-started: 2026-01-15
---

# 📚 Atomic Habits

## 📝 Key Takeaways
1. Habits are the compound interest of self-improvement
2. Focus on systems, not goals
3. Make it obvious, attractive, easy, satisfying

## 💡 Favorite Quotes
> "You do not rise to the level of your goals. You fall to the level of your systems."

## 🎯 Action Items
- [ ] Implement habit stacking for morning routine
- [ ] Design environment for good habits
- [ ] Track habits for 30 days
```

## 🔗 Linking & Discovery

### Encontrar Notas Relacionadas
```markdown
1. Abre una nota
2. Ctrl/Cmd + P → busca tu script de link-finder
3. Ejecuta el script
4. Revisa las sugerencias de enlaces
```

### Ejemplo de Query Compleja
```markdown
## 📊 Project Dashboard

### Active Projects by Priority
```dataview
TABLE 
  status as Status,
  progress + "%" as Progress,
  deadline as Deadline,
  length(file.tasks) as "Total Tasks",
  length(filter(file.tasks, (t) => !t.completed)) as "Open Tasks"
FROM "Projects"
WHERE status = "active"
SORT priority DESC, deadline ASC
```

### Recent Activity
```dataview
TABLE 
  file.mtime as "Last Modified",
  type as Type,
  tags as Tags
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 20
```
```

## 🎨 CSS Customization Examples

### Usar Callouts de Tarjeta
```markdown
> [!project] Website Redesign
> Status: Active
> Progress: 35%
> Deadline: 2026-03-15

> [!task] Important Task
> Priority: High
> Due: Tomorrow

> [!idea] New Feature Idea
> Category: Product
> Impact: High
```

### Tabla con Estilos
```markdown
<!-- Tabla compacta -->
<!-- {.compact-table} -->
| Name | Status | Priority |
|------|--------|----------|
| Task 1 | 🟢 Active | High |
| Task 2 | 🟡 Pending | Medium |
| Task 3 | 🔴 Blocked | Low |

<!-- Tabla con bordes -->
<!-- {.bordered-table} -->
| Metric | Q1 | Q2 | Q3 | Q4 |
|--------|----|----|----|----|
| Revenue | $100K | $120K | $150K | $180K |
| Users | 1K | 1.5K | 2K | 3K |
```

## 🤖 Script Usage

### Usar Funciones de Fecha
```markdown
<!-- En cualquier nota -->
Today: <% tp.user.insert_date() %>
Tomorrow: <% tp.user.insert_date("tomorrow") %>
Custom: <% tp.user.insert_date("custom", "DD/MM/YYYY") %>

Week number: <% tp.user.get_week_number() %>
Is weekend: <% tp.user.is_weekend() %>
```

### Crear Proyecto Completo
```markdown
1. Ctrl/Cmd + P → busca tu script create-project
2. Ejecuta el script
3. Ingresa el nombre del proyecto
4. Selecciona área y prioridad
5. El script crea:
   - Archivo principal del proyecto
   - Carpeta con subcarpetas (Tasks, Meetings, Documents)
   - Archivos de índice
   - Primera tarea
```

### Generar Reporte Semanal
```markdown
1. Al final de la semana
2. Ctrl/Cmd + P → busca weekly-review
3. Ejecuta el script
4. Se genera automáticamente:
   - Resumen de la semana
   - Tareas completadas
   - Proyectos actualizados
   - Reuniones
   - Métricas
```

## 🔄 Workflows Completos

### Workflow: Nueva Idea → Proyecto
```markdown
1. Captura idea con plantilla idea.md
2. Desarrolla la idea durante algunos días
3. Si es viable, convierte a proyecto:
   - Crea nuevo proyecto con project.md
   - Vincula la nota de idea original
   - Crea tareas iniciales
4. Trackea progreso regularmente
```

### Workflow: Meeting → Action Items → Tasks
```markdown
1. Antes de reunión: Crea nota con meeting.md
2. Durante reunión: Toma notas y lista action items
3. Después de reunión:
   - Crea tarea individual para cada action item
   - Vincula las tareas al meeting
   - Asigna responsables y fechas
4. Seguimiento: Actualiza estado en weekly review
```

### Workflow: Daily Notes → Weekly Review → Monthly Summary
```markdown
1. Diario: Completa daily note cada día
2. Semanal: 
   - Ejecuta weekly-review script
   - Revisa logros y desafíos
   - Planea próxima semana
3. Mensual:
   - Agrega todas las weekly reviews
   - Identifica patrones
   - Ajusta estrategias
```

## 🐍 Python Scripts

### Exportar Notas
```bash
# Exportar todas las notas a Markdown limpio
python Scripts/Python/export-notes.py \
  --vault /path/to/vault \
  --format markdown \
  --output ./export/ \
  --clean-links

# Exportar solo proyectos activos a HTML
python Scripts/Python/export-notes.py \
  --vault /path/to/vault \
  --format html \
  --output ./export/ \
  --filter "type:project" \
  --single-file

# Exportar a JSON para procesamiento
python Scripts/Python/export-notes.py \
  --vault /path/to/vault \
  --format json \
  --output ./export/
```

### Analizar Tags
```bash
# Análisis básico
python Scripts/Python/tag-analyzer.py \
  --vault /path/to/vault

# Generar reporte completo
python Scripts/Python/tag-analyzer.py \
  --vault /path/to/vault \
  --output tag-analysis.md \
  --suggest-merges

# Encontrar duplicados
python Scripts/Python/tag-analyzer.py \
  --vault /path/to/vault \
  --similarity-threshold 0.8 \
  --suggest-merges
```

### Backup del Vault
```bash
# Backup completo
python Scripts/Python/backup-vault.py \
  --vault /path/to/vault \
  --destination ~/Backups/

# Backup comprimido
python Scripts/Python/backup-vault.py \
  --vault /path/to/vault \
  --destination ~/Backups/ \
  --compress

# Backup con retención
python Scripts/Python/backup-vault.py \
  --vault /path/to/vault \
  --destination ~/Backups/ \
  --compress \
  --retention 30

# Listar backups existentes
python Scripts/Python/backup-vault.py \
  --vault /path/to/vault \
  --destination ~/Backups/ \
  --list
```

## 💡 Pro Tips

### 1. Hotkeys Personalizados
Configura hotkeys para acciones frecuentes:
- `Ctrl/Cmd + Shift + D` - Nueva daily note
- `Ctrl/Cmd + Shift + T` - Nueva tarea
- `Ctrl/Cmd + Shift + P` - Nuevo proyecto

### 2. Plantillas Anidadas
Reutiliza secciones comunes:
```markdown
<!-- En project.md -->
<% tp.file.include("[[_templates/_sections/status-section]]") %>
```

### 3. Variables Globales
Define en Templater settings:
```
author: Tu Nombre
company: Tu Empresa
```

Úsalas en plantillas:
```markdown
**Author**: <% tp.user.author %>
**Company**: <% tp.user.company %>
```

### 4. Queries Guardadas
Guarda queries complejas como snippets:
```markdown
```dataview
TABLE status, priority, deadline
FROM "Projects"
WHERE status = "active"
  AND priority = "high"
SORT deadline ASC
```
```

### 5. Tags Jerárquicos
Usa estructura consistente:
```markdown
#project/work/client
#area/personal/health
#resource/book/productivity
```

---

**¿Más ejemplos?** Consulta el README.md principal y los comentarios en los scripts para casos de uso avanzados.