import sys

if sys.modules.has_key('django'):
    from django.conf import settings
    import startup
    startup.start(settings)
