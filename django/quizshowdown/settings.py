import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_DIR = os.path.join(BASE_DIR, 'quizshowdown')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'djangobower',
    'compressor',
    'rest_framework',
    'quizshowdown.core',
)

BOWER_INSTALLED_APPS = (
    'ember-data#1.0.0-beta.7',
    'bootstrap#3.1.1',
    'handlebars#1.3.0',
    'ember-data-django-rest-adapter#1.0.1',
    'ember#1.5.0',
    'highlightjs#7.3.0',
    'jquery#2.0.3',
    'ember-addons.bs_for_ember#0.6.1'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'quizshowdown.urls'

WSGI_APPLICATION = 'quizshowdown.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(APP_DIR, "templates"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(APP_DIR, "static"),
)

COMPRESS_PRECOMPILERS = (
    ('text/x-handlebars', '{} {{infile}}'.format('django-ember-precompile')),
    ('text/coffeescript', '/Users/thoreg/node_modules/coffee-script/bin/coffee --compile --stdio'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(APP_DIR, 'collected_static/')

# registration
ACCOUNT_ACTIVATION_DAYS = 7
BOWER_COMPONENTS_ROOT = os.path.join(APP_DIR, 'components')

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
