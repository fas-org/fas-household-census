from django.conf.urls import url
from ..views import page9

urlpatterns = [
    url(r'^init$', page9.init, name='page9_init'),
    url(r'^$', page9.edit, name='page9_edit'),
    url(r'^(?P<pk>\d+|None)$', page9.edit, name='page9_edit'),
]