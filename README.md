# coder-85140-django

Proyecto final de blog en Django.

## Descripción

Aplicación web estilo blog programada en Python con Django. Incluye admin, perfiles, registro, páginas y formularios.

## Características

- Vista "Acerca de mí" en /about/
- Vista de blogs en /pages/
- Listado de páginas con "Leer más" para detalle
- Mensaje "No hay páginas aún" si no hay contenido
- Edición y borrado solo para usuarios logueados
- Autenticación: login, logout, registro
- Perfiles de usuario con avatar, bio, etc.
- Sistema de mensajería entre usuarios
- Herencia de templates con navbar
- Uso de CKEditor para contenido enriquecido
- Manejo de imágenes

## Instalación

1. Clona el repositorio
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno: `.venv\Scripts\activate`
4. Instala dependencias: `pip install -r requirements.txt`
5. Ejecuta migraciones: `python manage.py migrate`
6. Crea superusuario: `python manage.py createsuperuser`
7. Ejecuta servidor: `python manage.py runserver`

## Uso

- Accede a la aplicación en http://localhost:8000
- Regístrate o inicia sesión
- Crea páginas desde /pages/
- Envía mensajes a otros usuarios

## Tecnologías

- Django 6.0.2
- CKEditor
- Bootstrap 5
- SQLite

## Autor

[Tu nombre]