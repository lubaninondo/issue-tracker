from django.conf.urls import url
from .views import get_charts

urlpatterns = [
    url(r'^$', get_charts, name='get_charts'),
]