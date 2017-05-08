from django.conf.urls import url
from ..views import page8

urlpatterns = [
    url(r'^init$', page8.init, name='page8_init'),
    url(r'^$', page8.edit, name='page8_edit'),
    url(r'^(?P<pk>\d+|None)$', page8.edit, name='page8_edit'),
]