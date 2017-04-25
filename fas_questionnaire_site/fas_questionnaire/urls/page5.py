from django.conf.urls import url
from ..views import page5

urlpatterns = [
    url(r'^init$', page5.init, name='page5_init'),
    url(r'^$', page5.edit, name='page5_edit'),
    url(r'^(?P<pk>\d+|None)$', page5.edit, name='page5_edit'),
]