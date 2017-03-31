from django.conf.urls import url
from ..views import introduction

urlpatterns = [
    url(r'^new$', introduction.new, name='introduction_new'),
    url(r'^(?P<pk>\d+)/update$', introduction.update, name='introduction_update'),
    url(r'^get$', introduction.get, name='introduction_get'),
]