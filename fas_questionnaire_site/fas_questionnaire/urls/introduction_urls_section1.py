from django.conf.urls import url
from ..views import introduction_section1 as introduction

urlpatterns = [
    url(r'^$', introduction.new, name='introduction_new'),
    url(r'^init$', introduction.init, name='introduction_init'),
    url(r'^(?P<pk>\d+|None)$', introduction.edit, name='introduction_edit'),
    url(r'^get$', introduction.get, name='introduction_get'),
]