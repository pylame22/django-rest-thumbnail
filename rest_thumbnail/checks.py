from django.core.checks import Error, register
from django.urls.resolvers import RoutePattern, RegexPattern
from django.conf import settings as app_settings
from . import settings


@register()
def check_settings(app_configs, **kwargs):
    errors = []
    r = RoutePattern(settings.PATH) if settings.TYPE_PATTERN == settings.ROUTE else RegexPattern(settings.PATH)
    invalid_keys = [arg for arg in settings.PATH_REQUIRED_ARGS if arg not in r.regex.groupindex.keys()]
    if invalid_keys:
        errors.append(
            Error(
                'PATH in settings does not contains: ' + ', '.join(invalid_keys),
                obj=settings.PATH
            )
        )
    if not getattr(app_settings, 'MEDIA_ROOT', None):
        errors.append(Error('Set MEDIA_ROOT in settings'))
    return errors
