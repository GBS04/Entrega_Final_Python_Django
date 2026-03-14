# Proyecto final de blog en Django

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

## Uso / Orden de Pruebas

1. **Instalación y configuración inicial:**
   - Clona el repositorio.
   - Crea un entorno virtual: `python -m venv .venv`
   - Activa el entorno: `.venv\Scripts\activate` (Windows)
   - Instala dependencias: `pip install -r requirements.txt`
   - Ejecuta migraciones: `cd src && python manage.py migrate`
   - Crea superusuario: `python manage.py createsuperuser` (usa username=admin, password=123)
   - Ejecuta el servidor: `python manage.py runserver`

2. **Pruebas de funcionalidades:**
   - Accede a http://localhost:8000
   - Regístrate como usuario o inicia sesión con admin/123
   - Ve a /pages/ para ver el listado de páginas (usa la búsqueda para filtrar)
   - Crea una nueva página desde "Create New Page"
   - Edita o borra páginas (solo si estás logueado)
   - Ve a /accounts/profile/ para ver tu perfil
   - Edita tu perfil desde "Edit Profile"
   - Cambia tu password desde "Change Password"
   - Envía mensajes a otros usuarios desde /messaging/send/
   - Revisa inbox y mensajes enviados
   - Ve a /about/ para la página "Acerca de mí"
   - Accede al admin en /admin/ con admin/123

## Autor

Santiago Garcia Barcia
