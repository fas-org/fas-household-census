from django.conf.urls import url
from ..views import page21

urlpatterns = [
    url(r'^$', page21.new, name='page21_new'),
    url(r'^init$',page21.init,name='page21_init'),
    url(r'^(?P<pk>\d+|None)$',page21.edit,name='page21_edit'),
    url(r'^get$',page21.get,name='page21_get')
]
