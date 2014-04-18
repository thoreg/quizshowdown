from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%#c098o(yg1am!fg_9fxu$00kr$@@fn918x*=gq8tpzo6bxbx5'

COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/x-handlebars', '{} {{infile}}'.format('django-ember-precompile')),
    ('text/coffeescript', '/Users/thoreg/node_modules/coffee-script/bin/coffee --compile --stdio'),
)
