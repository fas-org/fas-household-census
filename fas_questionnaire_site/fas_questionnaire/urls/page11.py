from django.conf.urls import url
from ..views import page11

urlpatterns = [
    url(r'^init$', page11.init, name='page11_init'),
    url(r'^$', page11.init, name='page11_init'),
    url(r'^(?P<pk>\d+|None)$', page11.edit, name='page11_edit'),
]