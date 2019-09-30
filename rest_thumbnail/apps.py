from django.apps import AppConfig


class RestThumbnailConfig(AppConfig):
    name = 'rest_thumbnail'

    def ready(self):
        from . import signals  # noqa
        from . import checks  # noqa
