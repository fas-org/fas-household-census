from django.conf.urls import url
from ..views import page1 as page1

urlpatterns = [
    url(r'^$', page1.new, name='introduction_new'),
    url(r'^init$', page1.init, name='introduction_init'),
    url(r'^(?P<pk>\d+|None)$', page1.edit, name='introduction_edit'),
    url(r'^get$', page1.get, name='introduction_get'),
]