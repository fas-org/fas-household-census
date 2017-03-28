from django.conf.urls import url
from ..views import (HouseholdListView, HouseholdCreateView, HouseholdDetailView,
                     HouseholdUpdateView, HouseholdDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',
        # login_required(HouseholdCreateView.as_view()),
        HouseholdCreateView.as_view(),
        name="household_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HouseholdUpdateView.as_view()),
        name="household_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HouseholdDeleteView.as_view()),
        name="household_delete"),

    url(r'^(?P<pk>\d+)/$',
        HouseholdDetailView.as_view(),
        name="household_detail"),

    url(r'^$',
        HouseholdListView.as_view(),
        name="household_list"),
]
