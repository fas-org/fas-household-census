from django.conf.urls import url
from ..views import household as household

urlpatterns = [
    url(r'^$', household.new, name='household_new'),
    url(r'^init$', household.init, name='household_init'),
    url(r'^(?P<pk>\d+|None)$', household.edit, name='household_edit'),
    url(r'^get$', household.get, name='household_get'),
    url(r'^submit$', household.submit_household, name='household_submit'),
]