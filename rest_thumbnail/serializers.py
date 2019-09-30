from django.urls import reverse
from rest_framework.settings import api_settings
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail
from . import settings


class DynamicThumbnailField(serializers.ImageField):
    def __init__(self, *args, **kwargs):
        self.size = kwargs.pop('size', settings.DEFAULT_SIZE)
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        if not value:
            return None
        if settings.USE_NGINX:
            url = get_thumbnail(value, f'{self.size[0]}x{self.size[1]}', crop='center').url
        else:
            url = reverse('rest_thumbnail:detail', kwargs={'path': value, 'width': self.size[0], 'height': self.size[1]})
        use_url = getattr(self, 'use_url', api_settings.UPLOADED_FILES_USE_URL)
        if use_url and self.context.get('request'):
            request = self.context.get('request')
            return request.build_absolute_uri(url)
        return url
