from django.conf.urls import url
from ..views import ownership_section3 as ownership

urlpatterns = [
    url(r'^$', ownership.new, name='ownership_new'),
    url(r'^init$', ownership.init, name='ownership_init'),
    url(r'^(?P<pk>\d+|None)$', ownership.edit, name='ownership_edit'),
    url(r'^get$', ownership.get, name='ownership_get'),
]