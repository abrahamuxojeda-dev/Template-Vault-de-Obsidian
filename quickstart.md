# 🚀 Quick Start Guide

Esta guía te ayudará a poner en marcha el sistema de Obsidian en **15 minutos**.

## ✅ Pre-requisitos

- Obsidian instalado (versión 1.0+)
- Acceso a Community Plugins habilitado

## 📦 Paso 1: Instalar Plugins (5 min)

1. Abre Obsidian → **Settings** (⚙️)
2. Ve a **Community plugins**
3. Click en **Turn on community plugins** si está desactivado
4. Click en **Browse** y busca e instala:

### Esenciales
- [ ] **Templater** - Plantillas dinámicas
- [ ] **Dataview** - Queries de datos
- [ ] **Calendar** - Vista de calendario
- [ ] **Tasks** - Gestión de tareas

### Recomendados
- [ ] **QuickAdd** - Capturas rápidas
- [ ] **Periodic Notes** - Notas periódicas
- [ ] **Style Settings** - Personalización CSS
- [ ] **Tag Wrangler** - Gestión de tags

5. **Activa** todos los plugins instalados

## 📁 Paso 2: Copiar Archivos (5 min)

### Opción A: Copiar manualmente
1. Copia la carpeta `Templates/` a tu vault
2. Copia la carpeta `Scripts/` a tu vault
3. Copia los archivos `.css` de `CSS/` a `.obsidian/snippets/`

### Opción B: Usar línea de comandos
```bash
# Desde el directorio del sistema
cp -r Templates /ruta/a/tu/vault/
cp -r Scripts /ruta/a/tu/vault/
cp CSS/*.css /ruta/a/tu/vault/.obsidian/snippets/
```

## ⚙️ Paso 3: Configurar Plugins (5 min)

### Templater
1. Settings → Templater
2. **Template folder location**: `Templates`
3. **Script files folder location**: `Scripts/JavaScript`
4. Activa: ✅ **Trigger Templater on new file creation**
5. Activa: ✅ **Automatic jump to cursor**

### Dataview
1. Settings → Dataview
2. Activa: ✅ **Enable JavaScript Queries**
3. Activa: ✅ **Enable Inline Queries**

### Daily Notes
1. Settings → Daily notes
2. **New file location**: `Daily Notes/`
3. **Template file location**: `Templates/daily-note.md`
4. **Date format**: `YYYY-MM-DD`

### Tasks
1. Settings → Tasks
2. Configura el formato de tareas según prefieras

### Calendar
1. Settings → Calendar
2. **Weekly note folder**: `Weekly Notes/`
3. **Weekly note template**: (opcional)

## 🎨 Paso 4: Activar CSS Snippets

1. Settings → Appearance → **CSS snippets**
2. Activa los siguientes snippets:
   - [ ] `custom-theme.css`
   - [ ] `cards.css`
   - [ ] `tables.css`
3. Presiona el botón de **reload** (↻) si es necesario

## 🧪 Paso 5: Probar el Sistema

### Test 1: Crear Nota Diaria
1. Presiona el ícono de calendario
2. Click en hoy
3. Debería crearse automáticamente con la plantilla

### Test 2: Crear Proyecto
1. Abre Command Palette (`Ctrl/Cmd + P`)
2. Busca "Templater: Create new note from template"
3. Selecciona `project.md`
4. Completa el nombre del proyecto

### Test 3: Ejecutar Script
1. Abre una nota cualquiera
2. Command Palette → "Templater: Replace templates in the active file"
3. Inserta `<% tp.user.insert_date() %>`
4. Debería mostrar la fecha actual

## 📚 Próximos Pasos

Una vez instalado, consulta:

1. **README.md** - Documentación completa
2. **Templates/** - Explora todas las plantillas disponibles
3. **Scripts/** - Revisa los scripts y cómo usarlos

## 🆘 Solución de Problemas Comunes

### Los scripts no funcionan
**Solución**: Verifica que la ruta de scripts en Templater esté correcta: `Scripts/JavaScript`

### CSS no se aplica
**Solución**: 
1. Verifica que los snippets estén en `.obsidian/snippets/`
2. Actívalos en Settings → Appearance
3. Recarga Obsidian (`Ctrl/Cmd + R`)

### Plantillas no aparecen
**Solución**: Verifica que la carpeta `Templates` esté en la raíz de tu vault

### Errores de Templater
**Solución**:
1. Asegúrate de tener la última versión de Templater
2. Verifica que JavaScript esté habilitado en la configuración
3. Mira la consola de desarrollador (`Ctrl/Cmd + Shift + I`)

## ✨ Personalización Básica

### Cambiar colores del tema
Edita `custom-theme.css` líneas 15-45:
```css
.theme-light {
  --accent-color: #6366f1;  /* Cambia este valor */
  /* ... */
}
```

### Crear tu propia plantilla
1. Crea un nuevo archivo en `Templates/`
2. Añade frontmatter YAML
3. Usa sintaxis de Templater: `<% tp.date.now() %>`

### Añadir más snippets CSS
1. Crea archivo `.css` en `.obsidian/snippets/`
2. Escribe tu CSS personalizado
3. Actívalo en Settings → Appearance

## 📞 Necesitas Ayuda?

- Consulta el **README.md** completo
- Revisa los comentarios en los scripts
- Busca en [Obsidian Forum](https://forum.obsidian.md/)
- Revisa [Templater Docs](https://silentvoid13.github.io/Templater/)

---

**¡Listo!** 🎉 Ya tienes el sistema funcionando. Comienza creando tu primera nota diaria y explora las plantillas.