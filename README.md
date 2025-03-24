# Intro to Django

Connecting Django to a Postgres database.
Simple Pokedex application.

## Steps

### Environment setup
1. Create virtual environment and start it.
```python -m venv .venv```
```source .venv/bin/activate```

2. Install Django
```pip install django ```

3. Install dependencies and create requirements.txt
```pip install "psycopg[binary]" ```
```pip freeze > requirements.txt```

4. Initialize git and create .gitignore
```.venv```

### Django Setup
5. Start Django project
```django-admin```

6. Create new Django project
```python -m django startproject pokedex_proj```

7. Create new Django app
```python manage.py startapp pokemon_app```

8. Add the pokemon_app app to settings.py file

``` INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pokemon_app',
] ```

### Link PostgreSQL with Django
9. Create the database
```# bash
  createdb pokedex_db
# SQL 
  CREATE DATABASE pokedex_db;```

10. Set Postgres to default database
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pokedex_db',
    }
}```