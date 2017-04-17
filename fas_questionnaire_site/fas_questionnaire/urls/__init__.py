from django.conf.urls import url, include
from ..views import search


urlpatterns = [
    url(r'^household/', include('fas_questionnaire.urls.household_urls')),
    url(r'^introduction/', include('fas_questionnaire.urls.introduction_urls_section1')),
    url(r'^householdmembers/', include('fas_questionnaire.urls.householdmembers')),
    url(r'^page2/', include('fas_questionnaire.urls.page2')),
    url(r'^page3/', include('fas_questionnaire.urls.page3')),
    url(r'^page4/', include('fas_questionnaire.urls.page4')),
    url(r'^page5/', include('fas_questionnaire.urls.page5')),
    url(r'^page6/', include('fas_questionnaire.urls.page6')),
    url(r'^page8/', include('fas_questionnaire.urls.page8')),
    url(r'^page9/', include('fas_questionnaire.urls.page9')),
    url(r'^page11/', include('fas_questionnaire.urls.page11')),
    url(r'^page15/', include('fas_questionnaire.urls.page15')),
    url(r'^.*/search/$', search.search, name='search'),
    url(r'^othercosts/',include('fas_questionnaire.urls.othercosts')),
    url(r'^page22/',include('fas_questionnaire.urls.page22_urls')),
    url(r'^page13/',include('fas_questionnaire.urls.page_13')),
]