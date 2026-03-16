# Valentín Sánchez — Portafolio

Portafolio personal de Valentín Sánchez — Diseñador · Editor · Productor

## Stack
- HTML + CSS + JS puro (sin dependencias)
- Deploy en Vercel

---

## 🚀 Setup inicial (una sola vez)

### 1. Instalar herramientas
```bash
# Node.js (necesario para todo)
# Descargar desde: https://nodejs.org

# Vercel CLI
npm install -g vercel

# Claude Code
npm install -g @anthropic-ai/claude-code
```

### 2. Subir a GitHub
1. Ir a github.com → New repository → nombre: `portfolio-valentin`
2. En la terminal, dentro de esta carpeta:
```bash
git init
git add .
git commit -m "primer commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/portfolio-valentin.git
git push -u origin main
```

### 3. Conectar con Vercel
```bash
vercel
# Seguir los pasos → conectar con GitHub → deploy automático
```

Tu URL quedará algo como: `portfolio-valentin.vercel.app`

---

## ✏️ Editar con Claude Code (el flujo diario)

```bash
# Abrir la carpeta del proyecto en terminal, luego:
claude

# Ejemplos de lo que podés pedirle:
# "Agregá una sección de testimonios de clientes"
# "Cambiá el color de los botones a blanco con borde rojo"
# "Hacé el menú responsive para mobile"
# "Agregá un formulario de contacto"
# "Poné mi foto real en la sección sobre mí"
```

Cuando Claude Code termina los cambios:
```bash
git add .
git commit -m "descripcion del cambio"
git push
# Vercel se actualiza automáticamente en ~30 segundos
```

---

## 📁 Estructura
```
portfolio-valentin/
├── index.html      ← todo el portafolio
├── vercel.json     ← configuración de Vercel
└── README.md       ← estas instrucciones
```
