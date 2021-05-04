import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


def config():
    credentials = {
        'BASE_DIR': os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/karan",
        'SECRET_KEY': 'django-insecure-dz3!77g$mkgtsx3c5in6l*#t)v+1r=81l-9h0ecsu+9ss(g8)i',
        'DEBUG': True,
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travello',
        'USER': 'postgres',
        'PASSWORD': 'KARANM224',
        'HOST': 'localhost',
    }
    return credentials
