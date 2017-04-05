from django.conf.urls import url
from ..views import household_section1 as household

urlpatterns = [
    url(r'^$', household.new, name='household_new'),
    url(r'^(?P<pk>\d+)$', household.edit, name='household_edit'),
    url(r'^get$', household.get, name='household_get'),
]