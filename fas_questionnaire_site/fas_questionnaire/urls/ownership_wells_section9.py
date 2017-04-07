from django.conf.urls import url
from ..views import ownership_wells_section9 as ownership

urlpatterns = [
    url(r'^$', ownership.new, name='ownershipwells_new'),
    url(r'^init$', ownership.init, name='ownershipwells_init'),
    url(r'^(?P<pk>\d+|None)$', ownership.edit, name='ownershipwells_edit'),
    url(r'^get$', ownership.get, name='ownershipwells_get'),
]