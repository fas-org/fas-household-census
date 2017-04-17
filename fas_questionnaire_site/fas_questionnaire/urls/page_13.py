from django.conf.urls import url
from ..views import page_13

urlpatterns = [
    url(r'^$', page_13.new, name='page_13_new'),
    url(r'^init$', page_13.init, name='page_13_init'),
    url(r'^(?P<pk>\d+|None)$', page_13.edit, name='page_13_edit'),
]
