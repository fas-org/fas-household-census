from django.conf.urls import url
from ..views import householdmembers

urlpatterns = [
    url(r'^$', householdmembers.new, name='householdmembers_new'),
    url(r'^init$', householdmembers.init, name='householdmembers_init'),
    url(r'^(?P<pk>\d+|None)$', householdmembers.edit, name='householdmembers_edit'),
]
