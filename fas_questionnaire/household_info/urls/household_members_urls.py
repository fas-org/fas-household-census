from django.conf.urls import url
from ..views import (HouseholdMembersListView, HouseholdMembersCreateView, HouseholdMembersDetailView,
                     HouseholdMembersUpdateView, HouseholdMembersDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',
        # login_required(HouseholdMembersCreateView.as_view()),
        HouseholdMembersCreateView.as_view(),
        name="household_members_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(HouseholdMembersUpdateView.as_view()),
        name="household_members_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(HouseholdMembersDeleteView.as_view()),
        name="household_members_delete"),

    url(r'^(?P<pk>\d+)/$',
        HouseholdMembersDetailView.as_view(),
        name="household_members_detail"),

    url(r'^$',
        HouseholdMembersListView.as_view(),
        name="household_members_list"),
]
