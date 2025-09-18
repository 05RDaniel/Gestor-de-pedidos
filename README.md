# 📦 Gestor de Pedidos - Proyecto Django + Vue

Este proyecto es un sistema básico de **gestión de pedidos** y **logística**, desarrollado con **Django (backend)** y **Vue.js (frontend)**.  
Incluye un CRUD completo para pedidos y un sistema de reportes.

---

## 🚀 Requisitos previos

Antes de iniciar, asegúrese de tener instalado en su dispositivo:

- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js y npm](https://nodejs.org/)
- [Git](https://git-scm.com/)

> ⚠️ Durante la instalación de Python, marque la casilla **"Add Python to PATH"**.

---

## ⚙️ Configuración del Backend (Django)

1. Acceda a la carpeta del proyecto:
   ```bash
   cd gestor_pedidos/backend
   ```

2. Cree y active un entorno virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Instale las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecute las migraciones para preparar la base de datos SQLite:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Inicie el servidor de desarrollo de Django:
   ```bash
   python manage.py runserver
   ```

   El backend quedará disponible en:  
   👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Configuración del Frontend (Vue.js)

1. Acceda a la carpeta del frontend:
   ```bash
   cd gestor_pedidos/frontend
   ```

2. Instale las dependencias:
   ```bash
   npm install
   ```

3. Ejecute la aplicación en modo desarrollo:
   ```bash
   npm run serve
   ```

   El frontend quedará disponible en:  
   👉 [http://localhost:8080/](http://localhost:8080/)

---

## 🔄 Flujo de uso

1. Abra **http://localhost:8080/** en el navegador.
2. Desde el frontend podrá:
   - Crear pedidos
   - Listarlos en una tabla
   - Editarlos
   - Eliminarlos (con confirmación personalizada)

El backend expone la API en: **http://127.0.0.1:8000/api/**

---

## 📂 Estructura del proyecto

```
gestor_pedidos/
├── backend/        # Proyecto Django (API y lógica de negocio)
│   ├── orders/     # Aplicación principal (modelos, vistas, serializers)
│   ├── db.sqlite3  # Base de datos SQLite (autogenerada)
│   └── requirements.txt
├── frontend/       # Proyecto Vue.js (interfaz de usuario)
│   └── package.json
└── README.md
```

---

## 📌 Notas importantes

- El archivo `.gitignore` está configurado para evitar subir `venv/`, `node_modules/`, 
  archivos de caché y la base de datos SQLite.
- Para cambiar la base de datos a PostgreSQL u otra, actualice `settings.py` en el backend.
- Este proyecto es un ejemplo académico y puede ser ampliado con autenticación, 
  métricas avanzadas o despliegue en la nube.
