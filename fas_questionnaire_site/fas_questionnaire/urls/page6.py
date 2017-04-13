from django.conf.urls import url
from ..views import page6

urlpatterns = [
    url(r'^init$', page6.init, name='page6_init'),
    url(r'^$', page6.new, name='page6_new'),
    url(r'^(?P<pk>\d+|None)$', page6.edit, name='page6_edit'),
    url(r'^get$', page6.get, name='page6_get'),
]