from .base import *
# import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = True



# DATABASES = {'default': dj_database_url.config(
#     default='sqlite:////' + ROOT_DIR + '/dev.db')}

# EMAIL_BACKEND = ENV_SETTING('EMAIL_BACKEND',
#     'django.core.mail.backends.console.EmailBackend')

# # Disable caching while in development
# CACHES = {
#     'default': {
#         'BACKEND': ENV_SETTING('CACHE_BACKEND',
#             'django.core.cache.backends.dummy.DummyCache')
#     }
# }

# # Add SQL statement logging in development
# if (ENV_SETTING('SQL_DEBUG', 'false') == 'true'):
#     LOGGING['loggers']['django.db'] = {
#         'handlers': ['console'],
#         'level': 'DEBUG',
#         'propagate': False
#     }

# # set up Django Debug Toolbar if installed
# try:
#     import debug_toolbar  # noqa
#     MIDDLEWARE_CLASSES += (
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     )
#     INSTALLED_APPS += (
#         'debug_toolbar',
#     )
#     DEBUG_TOOLBAR_CONFIG = {
#         'INTERCEPT_REDIRECTS': False,
#         'SHOW_TOOLBAR_CALLBACK': lambda *args, **kwargs: True
#     }
# except ImportError:
#     pass


# # Set up django-extensions if installed
# try:
#     import django_extensions  # noqa
#     INSTALLED_APPS += ('django_extensions',)
# except ImportError:
#     pass

