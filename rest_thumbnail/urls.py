from . import settings
from .views import ThumbnailView

app_name = 'rest_thumbnail'

urlpatterns = [
    settings.ROUTE_FUNC(settings.PATH, ThumbnailView.as_view(), name='detail')
]
