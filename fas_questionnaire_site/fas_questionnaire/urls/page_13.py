from django.conf.urls import url
from ..views import page13

urlpatterns = [
    url(r'^$', page13.init, name='page13_init'),
    url(r'^init$', page13.init, name='page13_init'),
    url(r'^(?P<pk>\d+|None)$', page13.edit, name='page13_edit'),
]
