from .base import *

DEBUG = False

ADMINS = (
    ('Venturelli E.', 'jemanuelv@gmail.com'),
    )
    
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crud3',
        'USER': 'crud3',
        'PASSWORD': 'generis82',
    }
}