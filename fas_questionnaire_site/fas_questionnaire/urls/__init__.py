from django.conf.urls import url, include
from ..views import search


urlpatterns = [
    url(r'^household/', include('fas_questionnaire.urls.household_urls')),
    url(r'^introduction/', include('fas_questionnaire.urls.introduction_urls_section1')),
    url(r'^householdmembers/', include('fas_questionnaire.urls.householdmembers')),
    url(r'^page2/', include('fas_questionnaire.urls.page2')),
    url(r'^wells/', include('fas_questionnaire.urls.ownership_wells_section9')),
    url(r'^extension/', include('fas_questionnaire.urls.extension_urls_section8')),
    url(r'^cropProduction/',include('fas_questionnaire.urls.production_and_sales_on_operational_holding_urls_section6')),
    url(r'^landleasemortgage/', include('fas_questionnaire.urls.land_lease_mortgae_section5')),
    url(r'^.*/search/$', search.search, name='search'),
    url(r'^othercosts/',include('fas_questionnaire.urls.othercosts')),
    url(r'^page22/',include('fas_questionnaire.urls.page22_urls'))
]