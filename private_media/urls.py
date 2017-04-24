from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^{0}(?P<path>.*)$'.format(settings.PRIVATE_MEDIA_URL.lstrip('/')), views.serve_private_file),
]
