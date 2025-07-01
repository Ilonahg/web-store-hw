import os
from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасный заглушечный ключ (замени на свой в продакшне!)
SECRET_KEY = 'django-insecure-very-secret-key-for-dev-only'

# Включаем отладку (True для локальной разработки)
DEBUG = True

ALLOWED_HOSTS = []

# Подключённые приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # твои приложения
    'catalog',
    'blog',
    'users',
]



# Middleware — промежуточные обработчики
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL конфигурация проекта
ROOT_URLCONF = 'config.urls'

# Настройки шаблонов (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'config.wsgi.application'

# База данных: SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Язык и часовой пояс
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True

# Где будут статические файлы (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'catalog' / 'templates' / 'static']

# Где будут медиа-файлы (картинки из ImageField)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Автоматическое имя поля ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'users.CustomUser'
# Настройки почтового сервера
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'django20055@gmail.com'  # ← здесь укажи свою почту
EMAIL_HOST_PASSWORD = 'ybmh wvnz uorg isf '  # ← пароль приложения из Gmail
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
