from django.conf.urls import url
from ..views import page20

urlpatterns = [
    url(r'^init$', page20.init, name='page20_init'),
    url(r'^$', page20.init, name='page20_init'),
    url(r'^(?P<pk>\d+|None)$', page20.edit, name='page20_edit'),
]
