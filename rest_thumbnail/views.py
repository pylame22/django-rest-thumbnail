import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import Http404
from django.views import View
from sorl.thumbnail import get_thumbnail


class ThumbnailView(View):

    def get(self, request, *args, **kwargs):
        filepath = os.path.join(settings.MEDIA_ROOT, kwargs['path'])
        scale = f'{kwargs["width"]}x{kwargs["height"]}'
        image = get_thumbnail(filepath, scale, crop='center', quality=90)
        if image.size is None:
            raise Http404
        response = HttpResponse(image.read(), content_type='image/jpeg')
        response['Content-Disposition'] = 'inline; filename=' + image.name.split('/')[-1]
        return response
