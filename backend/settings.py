import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB", "bobyard_db"),
        'USER': os.getenv("POSTGRES_USER", "user"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD", "password"),
        'HOST': 'db',
        'PORT': '5432',
    }
}
