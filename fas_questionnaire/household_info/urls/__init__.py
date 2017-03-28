from django.conf.urls import include, url

urlpatterns = [
    url(r'^info/', include('household_info.urls.household_urls')),
    url(r'^members/', include('household_info.urls.household_members_urls')),
]
