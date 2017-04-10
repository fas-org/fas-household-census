from django.conf.urls import url
from ..views import land_lease_mortgage_section5 as landleasemortgage

urlpatterns = [
    url(r'^$', landleasemortgage.new, name='landleasemortgage_new'),
    url(r'^init$', landleasemortgage.init, name='landleasemortgage_init'),
    url(r'^(?P<pk>\d+|None)$', landleasemortgage.edit, name='landleasemortgage_edit'),
    url(r'^get$', landleasemortgage.get, name='landleasemortgage_get'),
]