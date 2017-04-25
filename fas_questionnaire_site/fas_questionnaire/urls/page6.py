from django.conf.urls import url
from ..views import page6

urlpatterns = [
    url(r'^init$', page6.init, name='page6_init'),
    url(r'^$', page6.edit, name='page6_edit'),
    url(r'^(?P<pk>\d+|None)$', page6.edit, name='page6_edit'),
]