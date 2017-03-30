from django.conf.urls import include, url
from ..views import home_view

urlpatterns = [
    url(r'^$', home_view.init, name='home'),
]