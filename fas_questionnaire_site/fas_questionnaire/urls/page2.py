from django.conf.urls import url
from ..views import page2

urlpatterns = [
    url(r'^init$', page2.init, name='page2_init'),
    url(r'^$', page2.edit, name='page2_edit'),
    url(r'^(?P<pk>\d+|None)$', page2.edit, name='page2_edit'),
]
