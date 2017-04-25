from django.conf.urls import url
from ..views import page19

urlpatterns = [
    url(r'^$', page19.init, name='page19_init'),
    url(r'^init$', page19.init, name='page19_init'),
    url(r'^(?P<pk>\d+|None)$', page19.edit, name='page19_edit'),
]
