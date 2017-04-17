from django.conf.urls import url
from ..views import page1

urlpatterns = [
    url(r'^$', page1.init, name='page1_init'),
    url(r'^init$', page1.init, name='page1_init'),
    url(r'^(?P<pk>\d+|None)$', page1.edit, name='page1_edit'),
    url(r'^get$', page1.get, name='page1_get'),
]