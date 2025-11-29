# Personalización Visual - Tienda Mixta La 40

## 🎨 Archivos CSS Personalizados Creados

### 1. **`custom.css`** - Estilos principales
- **Colores de marca**: Verde bosque (#2c5530) como color primario, dorado/beige (#d4a574) como secundario
- **Formas**: Bordes redondeados (8px-16px), sombras suaves
- **Componentes**: Navbar, botones, tarjetas, formularios, sidebar, tablas, modales
- **Efectos**: Gradientes, transiciones suaves, animaciones

### 2. **`login.css`** - Página de login personalizada
- **Fondo**: Gradiente verde con patrón decorativo sutil
- **Tarjeta de login**: Cristal esmerilado con bordes dorados
- **Campos**: Estilo moderno con iconos y efectos focus
- **Botones**: Gradientes con efectos hover y animaciones
- **Responsive**: Adaptable a móviles y tablets

### 3. **`fonts.css`** - Tipografía personalizada
- **Fuente principal**: Inter (moderna y legible)
- **Fuente para títulos**: Poppins (elegante)
- **Configuración**: Tamaños, pesos, interlineado optimizados
- **Responsive**: Ajustes automáticos para móviles

### 4. **`assets.css`** - Logos y assets
- **Configuración de logos**: Diferentes tamaños para navbar, login, favicon
- **Iconos**: Clases utilitarias para iconos personalizados
- **Efectos**: Hover y transiciones para imágenes
- **Responsive**: Adaptación automática de tamaños

## 📁 Estructura de Directorios Creada

```
apps/tienda_mixta/tienda_mixta/public/
├── css/
│   ├── custom.css      # Estilos principales del sistema
│   ├── login.css       # Estilos específicos de login
│   ├── fonts.css       # Configuración de tipografías
│   └── assets.css      # Configuración de logos y assets
├── images/             # Directorio para logos e imágenes
│   ├── logo.png        # Logo principal (AGREGAR)
│   ├── favicon.ico     # Icono del navegador (AGREGAR)
│   └── logo-white.png  # Logo blanco para navbar (AGREGAR)
└── js/                 # Scripts personalizados (futuro)
```

## 🖼️ Logos a Agregar

Para completar la personalización, agrega estos archivos en `/apps/tienda_mixta/tienda_mixta/public/images/`:

1. **`logo.png`** - Logo principal (recomendado: 200x80px, PNG con transparencia)
2. **`favicon.ico`** - Icono del navegador (32x32px, formato ICO)
3. **`logo-white.png`** - Logo blanco para navbar oscuro (200x80px, PNG)

## 🎨 Paleta de Colores Implementada

| Color | Hex | Uso |
|-------|-----|-----|
| Verde Principal | `#2c5530` | Navbar, botones primarios, títulos |
| Verde Claro | `#4a7c59` | Gradientes, hover states |
| Verde Oscuro | `#1e3a21` | Texto, bordes, estados activos |
| Dorado Principal | `#d4a574` | Acentos, botones secundarios |
| Dorado Claro | `#e6c299` | Fondos sutiles, hover states |
| Dorado Oscuro | `#b8924f` | Bordes, estados pressed |

## 🔧 Comandos para Aplicar Cambios

Ejecuta estos comandos después de agregar los logos:

```bash
# 1. Construir los assets
bench build --app tienda_mixta

# 2. Limpiar caché
bench clear-cache

# 3. Reiniciar el servidor
bench restart

# 4. Forzar recarga de assets (si es necesario)
bench migrate
```

## ✨ Características Implementadas

### Login Page
- ✅ Fondo con gradiente verde personalizado
- ✅ Tarjeta de cristal esmerilado
- ✅ Campos con iconos y efectos modernos
- ✅ Botones con gradientes y animaciones
- ✅ Enlaces con subrayado animado
- ✅ Responsive design completo

### Sistema Principal
- ✅ Navbar con gradiente verde y borde dorado
- ✅ Botones primarios con gradientes
- ✅ Tarjetas con sombras y bordes redondeados
- ✅ Formularios con campos estilizados
- ✅ Sidebar con efectos hover
- ✅ Tablas con encabezados verdes

### Tipografía
- ✅ Inter como fuente principal
- ✅ Poppins para títulos
- ✅ Tamaños y pesos optimizados
- ✅ Responsive typography

## 🚀 Próximos Pasos

1. **Agregar logos** en el directorio `/images/`
2. **Ejecutar comandos** de build y restart
3. **Probar en diferentes dispositivos**
4. **Ajustar colores** si es necesario
5. **Personalizar componentes específicos** según necesidades

## 🛠️ Personalización Adicional

Para modificar colores, edita las variables CSS en `custom.css`:
```css
:root {
    --tienda-primary: #tu_color_aqui;
    --tienda-secondary: #tu_color_aqui;
    /* etc... */
}
```

Los archivos están organizados de manera modular para facilitar futuras modificaciones y mantenimiento.