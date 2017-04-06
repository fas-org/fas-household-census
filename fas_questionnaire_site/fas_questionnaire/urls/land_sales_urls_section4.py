from django.conf.urls import url
from ..views import land_sales_section4 as landsales

urlpatterns = [
    url(r'^$', landsales.new, name='landsales_new'),
    url(r'^(?P<pk>\d+|None)$', landsales.edit, name='landsales_edit'),
    url(r'^get$', landsales.get, name='landsales_get'),
]