from django.conf.urls import url, include
from .views import create_comment

urlpatterns = [
    url(r'^comment/(?P<pk>\d+)$', create_comment, name='create_comment'),
]