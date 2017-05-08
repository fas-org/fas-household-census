from django.conf.urls import url
from ..views import page4 as page4

urlpatterns = [
    url(r'^$', page4.init, name='page4_init'),
    url(r'^init$', page4.init, name='page4_init'),
    url(r'^(?P<pk>\d+|None)$', page4.edit, name='page4_edit'),
]
