# Biblioteca

Aplicación de gestión de una biblioteca hecha con **Django 5.2**: libros, autores y editoriales, con buscador, área de usuarios y traducción español / inglés.

## Funcionalidades

- CRUD de **libros**, **autores** y **editoriales**, protegido por inicio de sesión.
- **Buscador** de libros.
- **Multidioma** (es / en) con `django-modeltranslation` y edición de traducciones con `django-rosetta`.
- Formularios maquetados con **Bootstrap 5** (`django-crispy-forms`).
- Middleware propio que mide el tiempo de procesamiento de cada petición.
- Acciones personalizadas en el panel de administración.

## Tecnologías

Python 3.12 · Django 5.2 · SQLite · Bootstrap 5 · django-crispy-forms · django-modeltranslation · django-rosetta

## Instalación

```bash
git clone https://github.com/angamadev/Biblioteca.git
cd Biblioteca
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata backup.json   # datos de ejemplo (opcional)
python manage.py runserver
```

Abre http://127.0.0.1:8000

Para producción, define la variable de entorno `DJANGO_SECRET_KEY` (ver `.env.example`).

## Estructura

```
biblioteca/   configuración, plantillas, formularios y estáticos
books/        modelos, vistas y URLs de libros, autores y editoriales
locale/       traducciones
```
