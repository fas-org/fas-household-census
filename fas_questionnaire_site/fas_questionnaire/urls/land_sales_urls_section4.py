from django.conf.urls import url
from ..views import land_sales_section4 as landsales

urlpatterns = [
    url(r'^init$', landsales.init, name='landsales_init'),
    url(r'^$', landsales.new, name='landsales_new'),
    url(r'^(?P<household>\d+|None)$', landsales.edit, name='landsales_edit'),
    url(r'^get$', landsales.get, name='landsales_get'),
]