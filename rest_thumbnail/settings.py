from django.conf import settings
from django.urls import path, re_path

ROUTE = 1
REGEX = 2
PATH_REQUIRED_ARGS = ['path', 'width', 'height']

if hasattr(settings, 'REST_THUMBNAIL_REGEX_PATH'):  # .../path/to/image.jpg@20x20
    PATH = getattr(settings, 'REST_THUMBNAIL_REGEX_PATH', r'^(?P<path>.+)@(?P<width>\d+)x(?P<height>\d+)$')
    ROUTE_FUNC = re_path
    TYPE_PATTERN = REGEX
else:
    PATH = getattr(settings, 'REST_THUMBNAIL_PATH', '<path:path>@<int:width>x<int:height>')
    ROUTE_FUNC = path
    TYPE_PATTERN = ROUTE

DEFAULT_SIZE = getattr(settings, 'REST_THUMBNAIL_DEFAULT_SIZE', (100, 100))
USE_NGINX = getattr(settings, 'REST_THUMBNAIL_USE_NGINX', True)
