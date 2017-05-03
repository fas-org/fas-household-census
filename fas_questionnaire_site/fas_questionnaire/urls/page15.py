from django.conf.urls import url
from ..views import page15

urlpatterns = [
    url(r'^init$', page15.init, name='page15_init'),
    url(r'^$', page15.init, name='page15_init'),
    url(r'^(?P<pk>\d+|None)$', page15.edit, name='page15_edit'),
]