# Templater Configuration Guide

Este archivo documenta la configuración recomendada para Templater.

## Settings → Templater

### General Settings

**Template folder location**
```
Templates
```
- Ruta donde se encuentran las plantillas
- Debe ser relativa a la raíz del vault

**Syntax highlighting**
```
✅ Enabled
```
- Resalta la sintaxis de Templater en el editor

### Template Hotkeys

Configura atajos de teclado para tus plantillas más usadas:

| Plantilla | Hotkey Sugerido | Uso |
|-----------|-----------------|-----|
| daily-note.md | `Ctrl/Cmd + Shift + D` | Nota diaria rápida |
| task.md | `Ctrl/Cmd + Shift + T` | Nueva tarea |
| meeting.md | `Ctrl/Cmd + Shift + M` | Nueva reunión |
| idea.md | `Ctrl/Cmd + Shift + I` | Captura de idea |

### Folder Templates

Aplica plantillas automáticamente cuando creas archivos en carpetas específicas:

| Carpeta | Plantilla |
|---------|-----------|
| `Daily Notes/` | `daily-note.md` |
| `Meetings/` | `meeting.md` |
| `Tasks/` | `task.md` |
| `Ideas/` | `idea.md` |
| `Books/` | `book.md` |

**Configuración:**
1. Ve a "Folder Templates"
2. Click en "Add New"
3. Selecciona carpeta y plantilla

### Startup Templates

**Empty file template**
```
❌ Disabled (opcional)
```
- Si lo habilitas, todos los archivos nuevos usarán una plantilla base

### User Script Functions

**Script files folder location**
```
Scripts/JavaScript
```
- Ruta donde se encuentran los scripts de usuario

**Enable JavaScript**
```
✅ Enabled
```
- Permite ejecutar scripts JavaScript personalizados

### System Commands

**Trigger Templater on new file creation**
```
✅ Enabled
```
- Ejecuta Templater automáticamente al crear archivos

**Automatic jump to cursor**
```
✅ Enabled
```
- Salta automáticamente a los cursores definidos en plantillas

**Enable folder templates**
```
✅ Enabled
```
- Activa el sistema de plantillas por carpeta

## User Scripts Setup

Los scripts deben exportar funciones que luego puedes usar en plantillas:

### Estructura de Script
```javascript
// insert-date.js
function insert_date(format = "default") {
    // ... implementación
    return formatted_date;
}

module.exports = insert_date;
// o
module.exports = { insert_date, other_function };
```

### Uso en Plantillas
```markdown
<% tp.user.insert_date() %>
<% tp.user.insert_date("custom", "DD/MM/YYYY") %>
```

## Commands Available

Una vez configurado, tendrás estos comandos disponibles:

### Via Command Palette (`Ctrl/Cmd + P`)

- **Templater: Insert Template** - Insertar plantilla en posición del cursor
- **Templater: Create new note from template** - Crear nueva nota con plantilla
- **Templater: Replace templates in the active file** - Procesar plantillas en archivo actual
- **Templater: Jump to next cursor location** - Saltar al siguiente cursor
- **Templater: Create new note from template (in new pane)** - Crear en panel nuevo

### Via Ribbon Icon

El ícono de Templater en la barra lateral izquierda abre el menú de plantillas.

## Custom Variables

Puedes definir variables personalizadas que estarán disponibles en todas tus plantillas:

### En Settings → Templater → User System Command Variables

Ejemplo:
```
Name: author
Value: Tu Nombre
```

Uso en plantillas:
```markdown
**Author**: <% tp.user.author %>
```

## Advanced Configuration

### Whitespace Control

Por defecto, Templater elimina espacios en blanco alrededor de los tags:

```markdown
<%- tag -%>  # Elimina espacios antes y después
<% tag -%>   # Elimina espacios después
<%- tag %>   # Elimina espacios antes
```

### Error Handling

Si un script falla, Templater mostrará el error en:
1. Notificación de Obsidian
2. Console (Ctrl/Cmd + Shift + I)

### Performance

- Los scripts grandes pueden afectar el rendimiento
- Considera usar async/await para operaciones pesadas
- Cachea resultados cuando sea posible

## Troubleshooting

### Scripts no se encuentran
**Solución**: Verifica que la ruta sea exacta: `Scripts/JavaScript` (sin `/` inicial)

### Errores de sintaxis
**Solución**: Revisa la sintaxis en la consola de desarrollador

### Plantillas no se aplican
**Solución**: 
1. Verifica que "Trigger on new file" esté activado
2. Asegúrate de que la carpeta de plantillas sea correcta
3. Recarga Obsidian

### Variables no definidas
**Solución**: Los scripts deben usar `module.exports` correctamente

## Example Configuration Summary

```yaml
Template Folder: Templates
Script Folder: Scripts/JavaScript
Trigger on new file: Yes
Auto jump to cursor: Yes
Folder templates: Yes
JavaScript enabled: Yes
```

## Best Practices

1. **Organización**: Mantén scripts y plantillas organizados en subcarpetas
2. **Nombres descriptivos**: Usa nombres claros para scripts y plantillas
3. **Documentación**: Comenta tus scripts con JSDoc
4. **Testing**: Prueba scripts en notas de prueba antes de usar en producción
5. **Backups**: Haz backup de tus scripts y plantillas regularmente

## Resources

- [Templater Documentation](https://silentvoid13.github.io/Templater/)
- [Templater Syntax](https://silentvoid13.github.io/Templater/introduction.html)
- [User Scripts Guide](https://silentvoid13.github.io/Templater/user-functions/overview.html)

---

**Nota**: Esta configuración es parte del sistema completo de Obsidian. Consulta README.md para más información.