# Sistema Completo para Obsidian
## 📚 Guía de Implementación

Este sistema proporciona un flujo de trabajo completo para Obsidian con plantillas, scripts y automatizaciones.

## 🎯 Características

- **Plantillas YAML**: 8 plantillas profesionales para diferentes tipos de notas
- **Scripts JavaScript**: Automatizaciones con Templater y Dataview
- **Scripts Python**: Procesamiento avanzado de notas
- **Snippets CSS**: Personalización visual del tema
- **Sistema de Tags**: Organización jerárquica inteligente
- **Daily Notes**: Sistema automático de notas diarias
- **Sistema de Proyectos**: GTD (Getting Things Done) integrado

## 📁 Estructura del Sistema

```
obsidian-vault/
├── .obsidian/
│   ├── plugins/
│   ├── snippets/
│   └── themes/
├── Templates/
│   ├── daily-note.md
│   ├── project.md
│   ├── meeting.md
│   ├── person.md
│   ├── book.md
│   ├── article.md
│   ├── idea.md
│   └── task.md
├── Scripts/
│   ├── JavaScript/
│   │   ├── insert-date.js
│   │   ├── create-project.js
│   │   ├── weekly-review.js
│   │   └── link-finder.js
│   └── Python/
│       ├── export-notes.py
│       ├── tag-analyzer.py
│       └── backup-vault.py
├── CSS/
│   ├── custom-theme.css
│   ├── cards.css
│   └── tables.css
└── Attachments/
```

## 🔌 Plugins Requeridos

### Esenciales
1. **Templater** - Para plantillas dinámicas
2. **Dataview** - Queries y vistas de datos
3. **Calendar** - Navegación de notas diarias
4. **Tasks** - Gestión de tareas
5. **Kanban** - Tableros visuales

### Recomendados
6. **QuickAdd** - Capturas rápidas
7. **Periodic Notes** - Notas semanales/mensuales
8. **Style Settings** - Personalización CSS
9. **Tag Wrangler** - Gestión de tags
10. **Natural Language Dates** - Fechas en lenguaje natural

## 🚀 Instalación Rápida

### Paso 1: Copiar Archivos
```bash
# Copiar plantillas
Templates/ → tu-vault/Templates/

# Copiar scripts
Scripts/ → tu-vault/Scripts/

# Copiar CSS snippets
CSS/*.css → tu-vault/.obsidian/snippets/
```

### Paso 2: Instalar Plugins
1. Abre Obsidian → Settings → Community Plugins
2. Desactiva "Restricted Mode"
3. Busca e instala los plugins listados arriba
4. Activa todos los plugins instalados

### Paso 3: Configurar Templater
1. Settings → Templater → Template folder location: `Templates`
2. Script files folder location: `Scripts/JavaScript`
3. Enable: "Trigger Templater on new file creation"
4. Enable: "Automatic jump to cursor"

### Paso 4: Configurar Snippets CSS
1. Settings → Appearance → CSS snippets
2. Activa los snippets que copiaste

### Paso 5: Configurar Daily Notes
1. Settings → Daily notes
2. Template file location: `Templates/daily-note.md`
3. New file location: `Daily Notes/`
4. Date format: `YYYY-MM-DD`

## 📝 Uso de Plantillas

### Crear Nota desde Plantilla
1. **Método 1 (Templater)**: `Alt+T` o `Cmd+T` → Selecciona plantilla
2. **Método 2 (Manual)**: Comando → "Templater: Insert Template"
3. **Método 3 (Automático)**: Crea archivo en carpeta específica

### Plantillas Disponibles

#### 1. Daily Note (Nota Diaria)
- Registro diario automático
- Secciones: Objetivos, Log, Tareas, Reflexiones
- Links a ayer/mañana automáticos

#### 2. Project (Proyecto)
- Metodología GTD
- Estados: planning, active, on-hold, completed, cancelled
- Tracking de progreso y deadlines

#### 3. Meeting (Reunión)
- Agenda estructurada
- Participantes y decisiones
- Action items automáticos

#### 4. Person (Contacto)
- CRM personal
- Interacciones y contexto
- Links a proyectos relacionados

#### 5. Book (Libro)
- Ficha de lectura
- Notas por capítulo
- Rating y reseña

#### 6. Article (Artículo)
- Lectura y análisis
- Resumen y citas
- Conexiones a otras notas

#### 7. Idea (Idea)
- Captura de ideas
- Estado y categoría
- Desarrollo y refinamiento

#### 8. Task (Tarea)
- Tarea individual
- Prioridad y contexto
- Subtareas y dependencias

## 🎨 Personalización CSS

### Snippets Disponibles

1. **custom-theme.css**: Tema principal con variables
2. **cards.css**: Estilo de tarjetas para callouts
3. **tables.css**: Tablas mejoradas con hover y zebra

### Modificar Colores
Edita las variables CSS en `custom-theme.css`:
```css
:root {
  --accent-color: #6366f1;
  --background-primary: #ffffff;
  --text-normal: #1f2937;
}
```

## 🤖 Scripts JavaScript

### insert-date.js
Inserta fecha actual en diferentes formatos
```javascript
// Uso en plantilla: <% tp.user.insert_date() %>
```

### create-project.js
Crea estructura completa de proyecto
```javascript
// Uso: Ejecutar desde Templater
```

### weekly-review.js
Genera reporte semanal automático
```javascript
// Uso: Ejecutar cada fin de semana
```

### link-finder.js
Encuentra notas relacionadas por contenido
```javascript
// Uso: En cualquier nota activa
```

## 🐍 Scripts Python

### export-notes.py
Exporta notas a diferentes formatos
```bash
python Scripts/Python/export-notes.py --format markdown --output ./export/
```

### tag-analyzer.py
Analiza uso de tags y sugiere consolidación
```bash
python Scripts/Python/tag-analyzer.py --vault ./
```

### backup-vault.py
Backup automático del vault
```bash
python Scripts/Python/backup-vault.py --destination ~/Backups/
```

## 📊 Queries Dataview Útiles

### Tareas Pendientes por Proyecto
```dataview
TASK
WHERE !completed
GROUP BY file.folder
SORT priority DESC
```

### Notas Recientes
```dataview
TABLE file.ctime as Creado, file.mtime as Modificado
FROM ""
SORT file.mtime DESC
LIMIT 10
```

### Proyectos Activos
```dataview
TABLE status, priority, deadline
FROM "Projects"
WHERE status = "active"
SORT priority DESC
```

## 🏷️ Sistema de Tags

### Categorías Principales
- `#project/` - Proyectos
- `#area/` - Áreas de responsabilidad
- `#resource/` - Recursos y referencias
- `#archive/` - Completado/archivado

### Tags de Estado
- `#status/active`
- `#status/planning`
- `#status/completed`
- `#status/on-hold`

### Tags de Prioridad
- `#priority/high`
- `#priority/medium`
- `#priority/low`

### Tags de Contexto
- `#context/work`
- `#context/personal`
- `#context/learning`

## 🔄 Flujos de Trabajo

### 1. Gestión de Proyectos
1. Crear proyecto con plantilla
2. Definir tareas con checkboxes
3. Actualizar estado regularmente
4. Revisar con weekly-review.js

### 2. Captura de Ideas
1. Usar plantilla de Idea
2. Tag apropiado (#idea/tech, #idea/business)
3. Desarrollar en sesiones dedicadas
4. Convertir a proyecto si procede

### 3. Notas de Lectura
1. Crear con plantilla Book o Article
2. Tomar notas mientras lees
3. Crear notas permanentes de conceptos
4. Vincular con Zettelkasten

### 4. Reuniones
1. Crear con plantilla Meeting antes
2. Tomar notas durante
3. Crear tareas de action items
4. Archivar después de seguimiento

## 🛠️ Troubleshooting

### Los scripts no funcionan
- Verifica que Templater esté configurado correctamente
- Revisa la ruta de Scripts/JavaScript
- Asegúrate de que la sintaxis sea válida

### CSS no se aplica
- Verifica que los snippets estén activados en Settings
- Recarga Obsidian (Ctrl+R)
- Revisa la consola de desarrollador (Ctrl+Shift+I)

### Plantillas no aparecen
- Verifica la ruta en configuración de Templater
- Asegúrate de que los archivos estén en Templates/
- Revisa permisos de archivos

## 📚 Recursos Adicionales

- [Documentación de Obsidian](https://help.obsidian.md/)
- [Templater Documentation](https://silentvoid13.github.io/Templater/)
- [Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/)
- [Obsidian Forum](https://forum.obsidian.md/)

## 🔮 Próximas Mejoras

- [ ] Integración con APIs externas
- [ ] Templates para MOCs (Maps of Content)
- [ ] Sistema de publicación a web
- [ ] Sincronización con calendario
- [ ] Generación automática de índices

## 📄 Licencia

Este sistema es de código abierto. Siéntete libre de modificar y adaptar a tus necesidades.

---

**Versión**: 1.0.0  
**Última actualización**: Febrero 2026  
**Autor**: AbrahamUxdev