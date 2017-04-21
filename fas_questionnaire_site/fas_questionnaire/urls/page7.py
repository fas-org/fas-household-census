from django.conf.urls import url
from ..views import page7

urlpatterns = [
    url(r'^init$', page7.init, name='page7_init'),
    url(r'^$', page7.init, name='page7_init'),
    url(r'^(?P<pk>\d+|None)$', page7.edit, name='page7_edit'),
]
