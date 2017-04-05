from django.conf.urls import url, include

urlpatterns = [
    url(r'^household/', include('fas_questionnaire.urls.household_urls')),
    url(r'^introduction/', include('fas_questionnaire.urls.introduction_urls_section1')),
    url(r'^landsales/', include('fas_questionnaire.urls.land_sales_urls_section4'))
]