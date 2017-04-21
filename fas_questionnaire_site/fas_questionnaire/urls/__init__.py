from django.conf.urls import url, include
from ..views import search



urlpatterns = [
    url(r'^household/', include('fas_questionnaire.urls.household_urls')),
    url(r'^page1/', include('fas_questionnaire.urls.page1')),
    url(r'^page2/', include('fas_questionnaire.urls.page2')),
    url(r'^page3/', include('fas_questionnaire.urls.page3')),
    url(r'^page4/', include('fas_questionnaire.urls.page4')),
    url(r'^page5/', include('fas_questionnaire.urls.page5')),
    url(r'^page6/', include('fas_questionnaire.urls.page6')),
    url(r'^page8/', include('fas_questionnaire.urls.page8')),
    url(r'^page9/', include('fas_questionnaire.urls.page9')),
    url(r'^page11/', include('fas_questionnaire.urls.page11')),
    url(r'^page13/',include('fas_questionnaire.urls.page_13')),
    url(r'^page15/', include('fas_questionnaire.urls.page15')),
    url(r'^page17/', include('fas_questionnaire.urls.page17')),
    url(r'^page21/', include('fas_questionnaire.urls.page21')),
    url(r'^page16/', include('fas_questionnaire.urls.page16')),
    url(r'^page22/',include('fas_questionnaire.urls.page22_urls')),
    url(r'^.*/search/$', search.search, name='search'),
    url(r'^page10/', include('fas_questionnaire.urls.page10')),
    url(r'^page18/', include('fas_questionnaire.urls.page18')),
]

