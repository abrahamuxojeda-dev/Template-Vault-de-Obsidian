# 📦 Sistema Completo para Obsidian

## 📚 Índice de Archivos

Bienvenido al sistema completo de Obsidian. Esta es tu guía para navegar todos los archivos incluidos.

---

## 🚀 Comienza Aquí

### 1. [QUICKSTART.md](QUICKSTART.md)
**⏱️ 15 minutos** - Instalación y configuración rápida
- Instalación de plugins
- Copia de archivos
- Configuración básica
- Primera prueba

### 2. [README.md](README.md)
**📖 Documentación completa** - Todo sobre el sistema
- Características
- Estructura
- Configuración detallada
- Troubleshooting

### 3. [EXAMPLES.md](EXAMPLES.md)
**💡 Ejemplos prácticos** - Aprende con casos reales
- Workflows completos
- Casos de uso
- Queries Dataview
- Scripts en acción

### 4. [TEMPLATER-CONFIG.md](TEMPLATER-CONFIG.md)
**⚙️ Configuración de Templater** - Guía técnica
- Settings recomendados
- Configuración de scripts
- Folder templates
- Hotkeys

---

## 📁 Estructura del Sistema

```
obsidian-system/
│
├── 📄 README.md                    # Documentación principal
├── 📄 QUICKSTART.md               # Guía de inicio rápido
├── 📄 EXAMPLES.md                 # Ejemplos de uso
├── 📄 TEMPLATER-CONFIG.md        # Config de Templater
│
├── 📂 Templates/                  # Plantillas con YAML
│   ├── daily-note.md             # Nota diaria automática
│   ├── project.md                # Gestión de proyectos GTD
│   ├── meeting.md                # Notas de reuniones
│   ├── task.md                   # Tareas individuales
│   ├── person.md                 # CRM personal
│   ├── book.md                   # Notas de lectura
│   ├── article.md                # Artículos y recursos
│   └── idea.md                   # Captura de ideas
│
├── 📂 Scripts/
│   ├── 📂 JavaScript/            # Scripts para Templater
│   │   ├── insert-date.js        # Utilidades de fecha
│   │   ├── create-project.js     # Crear proyecto completo
│   │   ├── weekly-review.js      # Reporte semanal
│   │   └── link-finder.js        # Encontrar notas relacionadas
│   │
│   └── 📂 Python/                # Scripts de automatización
│       ├── export-notes.py       # Exportar a múltiples formatos
│       ├── tag-analyzer.py       # Análisis de tags
│       └── backup-vault.py       # Sistema de backups
│
└── 📂 CSS/                       # Snippets de personalización
    ├── custom-theme.css          # Tema principal
    ├── cards.css                 # Estilo de tarjetas
    └── tables.css                # Tablas mejoradas
```

---

## 📋 Plantillas (Templates/)

### 🗓️ [daily-note.md](Templates/daily-note.md)
**Sistema de notas diarias**
- Intención del día
- Prioridades
- Log por bloques de tiempo
- Gratitud y reflexión
- Métricas diarias
- Rating del día

**Uso**: Automático con Calendar plugin o Daily Notes

---

### 📊 [project.md](Templates/project.md)
**Gestión completa de proyectos**
- Metodología GTD
- Objetivos y KRs
- Timeline y milestones
- Tareas y deliverables
- Stakeholders
- Tracking de progreso

**Uso**: `Templater: Create new note from template`

---

### 🤝 [meeting.md](Templates/meeting.md)
**Notas de reuniones estructuradas**
- Agenda detallada
- Asistentes
- Notas por tema
- Action items
- Decisiones tomadas
- Follow-up

**Uso**: Antes de cada reunión

---

### ✅ [task.md](Templates/task.md)
**Tareas individuales con tracking**
- Subtasks
- Dependencias
- Recursos necesarios
- Work log
- Timeline

**Uso**: Para tareas complejas que necesitan documentación

---

### 👤 [person.md](Templates/person.md)
**CRM personal**
- Información de contacto
- Contexto profesional
- Historial de interacciones
- Proyectos compartidos
- Notas importantes

**Uso**: Para contactos importantes

---

### 📚 [book.md](Templates/book.md)
**Sistema de lectura**
- Metadata del libro
- Notas por capítulo
- Conceptos clave
- Quotes favoritas
- Actionables
- Rating y review

**Uso**: Al comenzar un nuevo libro

---

### 📄 [article.md](Templates/article.md)
**Notas de artículos/recursos**
- Metadata y fuente
- Resumen ejecutivo
- Análisis crítico
- Conexiones
- Action items

**Uso**: Para artículos importantes

---

### 💡 [idea.md](Templates/idea.md)
**Captura y desarrollo de ideas**
- Concepto central
- Assessment rápido
- Variaciones
- Next steps
- Decision tracking

**Uso**: Cuando tienes una idea nueva

---

## 🤖 Scripts JavaScript (Scripts/JavaScript/)

### 📅 [insert-date.js](Scripts/JavaScript/insert-date.js)
**Utilidades avanzadas de fecha**

**Funciones disponibles**:
- `insert_date(format)` - Múltiples formatos de fecha
- `get_week_dates()` - Fechas de la semana
- `get_month_dates()` - Fechas del mes
- `days_until(date)` - Días hasta fecha
- `days_since(date)` - Días desde fecha
- `get_time_block()` - Bloque horario actual
- `working_days_between()` - Días laborables

**Uso en plantillas**:
```markdown
<% tp.user.insert_date() %>
<% tp.user.insert_date("week") %>
<% tp.user.get_time_block() %>
```

---

### 🏗️ [create-project.js](Scripts/JavaScript/create-project.js)
**Crear estructura completa de proyecto**

**Crea automáticamente**:
- Archivo principal del proyecto
- Carpetas organizadas (Tasks, Meetings, Documents, Resources)
- Archivos de índice con Dataview
- Primera tarea setup
- Configuración inicial

**Uso**: Ejecutar desde Command Palette

---

### 📊 [weekly-review.js](Scripts/JavaScript/weekly-review.js)
**Generador de reporte semanal**

**Genera automáticamente**:
- Resumen de la semana
- Tareas completadas
- Progreso de proyectos
- Reuniones
- Reflexiones
- Plan para próxima semana

**Uso**: Ejecutar cada viernes/domingo

---

### 🔗 [link-finder.js](Scripts/JavaScript/link-finder.js)
**Encuentra notas relacionadas**

**Características**:
- Análisis de contenido
- Comparación de keywords
- Tags compartidos
- Scoring de similaridad
- Sugerencias de enlaces

**Uso**: Ejecutar en cualquier nota

---

## 🐍 Scripts Python (Scripts/Python/)

### 📤 [export-notes.py](Scripts/Python/export-notes.py)
**Exportación de notas a múltiples formatos**

**Formatos soportados**:
- Markdown (limpio)
- HTML (con estilos)
- JSON (estructurado)
- Plain text

**Uso**:
```bash
python export-notes.py --vault /path --format html --output ./export/
```

---

### 🏷️ [tag-analyzer.py](Scripts/Python/tag-analyzer.py)
**Análisis completo de tags**

**Funciones**:
- Estadísticas de uso
- Tags similares/duplicados
- Tags huérfanos
- Análisis de jerarquía
- Sugerencias de merge
- Reporte detallado

**Uso**:
```bash
python tag-analyzer.py --vault /path --suggest-merges
```

---

### 💾 [backup-vault.py](Scripts/Python/backup-vault.py)
**Sistema automático de backups**

**Características**:
- Backup completo o incremental
- Compresión zip
- Retention policy
- Verificación de integridad
- Lista de backups

**Uso**:
```bash
python backup-vault.py --vault /path --destination ~/Backups/ --compress
```

---

## 🎨 CSS Snippets (CSS/)

### 🎨 [custom-theme.css](CSS/custom-theme.css)
**Tema principal personalizado**

**Incluye**:
- Paleta de colores (light/dark)
- Tipografía mejorada
- Links y headers
- Code blocks
- Blockquotes
- Tags
- Scrollbars
- Animaciones

**Activar**: Settings → Appearance → CSS snippets

---

### 🃏 [cards.css](CSS/cards.css)
**Callouts estilo tarjeta**

**Tipos especiales**:
- `[!project]` - Card de proyecto
- `[!task]` - Card de tarea
- `[!meeting]` - Card de reunión
- `[!idea]` - Card de idea
- `[!goal]` - Card de objetivo
- Grid layouts
- Progress bars

**Uso**:
```markdown
> [!project] Mi Proyecto
> Contenido de la tarjeta
```

---

### 📊 [tables.css](CSS/tables.css)
**Tablas profesionales**

**Características**:
- Hover effects
- Zebra striping
- Sticky headers
- Color-coded cells
- Status indicators
- Sortable columns
- Responsive design

**Clases disponibles**:
- `.compact-table` - Tabla compacta
- `.bordered-table` - Con bordes
- `.minimal-table` - Estilo minimalista

---

## 🎯 Workflows Recomendados

### 📅 Daily Workflow
1. **Mañana**: Abre daily note, establece intención y prioridades
2. **Durante el día**: Log de actividades
3. **Noche**: Reflexión y rating del día

### 🗓️ Weekly Workflow
1. **Lunes**: Revisa weekly goals
2. **Durante semana**: Update de proyectos
3. **Viernes**: Ejecuta weekly-review.js

### 📊 Project Workflow
1. **Inicio**: Crea proyecto con create-project.js
2. **Desarrollo**: Update regular de progreso
3. **Reuniones**: Link meeting notes
4. **Cierre**: Completa sección final

### 💡 Idea Workflow
1. **Captura**: Usa idea.md template
2. **Desarrollo**: Añade notas y variaciones
3. **Decisión**: Go/No-Go
4. **Conversión**: Si es viable → proyecto

---

## ⚡ Quick Reference

### Hotkeys Sugeridos
- `Ctrl/Cmd + Shift + D` → Daily note
- `Ctrl/Cmd + Shift + T` → Nueva tarea
- `Ctrl/Cmd + Shift + M` → Nueva reunión
- `Ctrl/Cmd + Shift + P` → Nuevo proyecto

### Templater Syntax
```markdown
<% tp.date.now() %>              # Fecha actual
<% tp.file.cursor() %>           # Cursor position
<% tp.user.insert_date() %>      # Custom date function
<% tp.system.prompt("Name") %>   # User input
```

### Dataview Queries
```markdown
```dataview
TABLE status, priority
FROM "Projects"
WHERE status = "active"
SORT priority DESC
```
```

---

## 🔧 Mantenimiento

### Backups Regulares
```bash
# Semanal
python Scripts/Python/backup-vault.py --vault . --destination ~/Backups/ --compress --retention 30
```

### Análisis de Tags
```bash
# Mensual
python Scripts/Python/tag-analyzer.py --vault . --output tag-analysis.md --suggest-merges
```

### Limpieza
- Revisa tags huérfanos
- Actualiza proyectos completados
- Archiva notas antiguas

---

## 🆘 Soporte

### Documentación
- [README.md](README.md) - Doc completa
- [QUICKSTART.md](QUICKSTART.md) - Inicio rápido
- [EXAMPLES.md](EXAMPLES.md) - Ejemplos prácticos

### Recursos Externos
- [Obsidian Forum](https://forum.obsidian.md/)
- [Templater Docs](https://silentvoid13.github.io/Templater/)
- [Dataview Docs](https://blacksmithgu.github.io/obsidian-dataview/)

### Troubleshooting
Ver sección en README.md

---

## 📝 Notas Finales

Este sistema es completamente **modular y personalizable**. No necesitas usar todo de una vez:

1. **Empieza simple**: Instala plugins y usa 1-2 plantillas
2. **Expande gradualmente**: Añade más plantillas según necesites
3. **Personaliza**: Modifica templates, scripts y CSS a tu gusto
4. **Itera**: El sistema mejora con el uso

**¡Disfruta tu sistema de productividad!** 🚀

---

**Versión**: 1.0.0  
**Última actualización**: Febrero 2026  
**Licencia**: Open Source - Modifica y comparte libremente