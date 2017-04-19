from django.conf.urls import url
from ..views import page10

urlpatterns = [
    url(r'^$', page10.new, name='page10_new'),
    url(r'^init$', page10.init, name='page10_init'),
    url(r'^(?P<pk>\d+|None)$', page10.edit, name='page10_edit'),
]
