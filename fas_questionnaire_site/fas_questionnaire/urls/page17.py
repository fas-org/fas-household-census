from django.conf.urls import url
from ..views import page17 as page17

urlpatterns = [
    url(r'^$', page17.init, name='page17_init'),
    url(r'^init$', page17.init, name='page17_init'),
    url(r'^(?P<pk>\d+|None)$', page17.edit, name='page17_edit'),
]