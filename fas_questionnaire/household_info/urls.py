from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.household_new, name='household_new'),
    url(r'^members/new/$', views.household_members_new, name='household_members_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.household_edit, name='household_edit'),
    url(r'^members/(?P<pk>\d+)/edit/$', views.household_members_edit, name='household_members_edit'),
]
