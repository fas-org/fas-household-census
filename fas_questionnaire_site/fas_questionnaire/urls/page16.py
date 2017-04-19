from django.conf.urls import url
from ..views import page16

urlpatterns = [
    url(r'^init$', page16.init, name='page16_init'),
    url(r'^$', page16.new, name='page16_new'),
    url(r'^(?P<pk>\d+|None)$', page16.edit, name='page16_edit'),
]