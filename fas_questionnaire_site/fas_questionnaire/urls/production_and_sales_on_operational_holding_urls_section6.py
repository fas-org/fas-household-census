from django.conf.urls import url
from ..views import production_and_sales_on_operational_holding_section6 as cropProduction

urlpatterns = [
    url(r'^$', cropProduction.new, name='production_and_sales_on_operational_holding_new'),
    url(r'^init$', cropProduction.init, name='production_and_sales_on_operational_holding_init'),
    url(r'^(?P<pk>\d+|None)$', cropProduction.edit, name='production_and_sales_on_operational_holding_edit'),
    url(r'^get$', cropProduction.get, name='production_and_sales_on_operational_holding_get'),
]