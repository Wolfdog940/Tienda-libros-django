DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'LIBRERIA_DB',
        'USER': 'root',
        'PASSWORD': 'Urrutia@940',
        'HOST': 'localhost',  # o la IP de tu servidor MySQL
        'PORT': '3306',       # puerto de MySQL
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
