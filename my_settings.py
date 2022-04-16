DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wanted',
        'USER': 'root',
        'PASSWORD': 'liminxi',
        'HOST': '127.0.0.1',
        'PORT': '3306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-b0$@f30ginik1egbk$z!wpb8-*1l(uoul2!+p*y(9)-8j$7@#*'