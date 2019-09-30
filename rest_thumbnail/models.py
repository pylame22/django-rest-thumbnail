import os
from django.db import models
from sorl.thumbnail import get_thumbnail
from django.conf import settings as app_settings


class ThumbnailImageField(models.ImageField):
    def __init__(self, *args, **kwargs):
        self.sizes = kwargs.pop('sizes', None)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        file = super().pre_save(model_instance, add)
        if file and self.sizes:
            filepath = os.path.join(app_settings.MEDIA_ROOT, file.name)
            for _, size in self.sizes:
                get_thumbnail(filepath, f'{size[0]}x{size[1]}', crop='center', quality=90)
        return file
