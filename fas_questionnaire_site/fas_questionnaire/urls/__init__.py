from django.conf.urls import url, include
from ..views import search


urlpatterns = [
    url(r'^household/', include('fas_questionnaire.urls.household_urls')),
    url(r'^introduction/', include('fas_questionnaire.urls.introduction_urls_section1')),
    url(r'^householdmembers/', include('fas_questionnaire.urls.householdmembers')),
    url(r'^landsales/', include('fas_questionnaire.urls.land_sales_urls_section4')),
    url(r'^ownership/', include('fas_questionnaire.urls.ownership_section3')),
    url(r'^wells/', include('fas_questionnaire.urls.ownership_wells_section9')),
    url(r'^extension/', include('fas_questionnaire.urls.extension_urls_section8')),
    url(r'^.*/search/$', search.search, name='search'),
]