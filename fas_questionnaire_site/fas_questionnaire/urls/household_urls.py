from django.conf.urls import url
from ..views import household

urlpatterns = [
    url(r'^save$', household.save, name='household_save'),
]