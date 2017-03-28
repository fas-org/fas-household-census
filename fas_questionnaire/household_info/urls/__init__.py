from django.conf.urls import include, url

urlpatterns = [
    url(r'', include('household_info.urls.household_urls')),  # NOQA
]
