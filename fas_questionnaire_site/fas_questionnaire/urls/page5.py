from django.conf.urls import url
from ..views import page5

urlpatterns = [
    url(r'^init$', page5.init, name='page5_init'),
    url(r'^$', page5.new, name='page5_new'),
    url(r'^(?P<pk>\d+|None)$', page5.edit, name='page5_edit'),
    url(r'^get$', page5.get, name='page5_get'),
]