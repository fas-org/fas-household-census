from django.conf.urls import url
from ..views import othercosts

urlpatterns = [
    url(r'^$', othercosts.new, name='othercosts_new'),
    url(r'^init$', othercosts.init, name='othercosts_init'),
    url(r'^(?P<pk>\d+|None)$', othercosts.edit, name='othercosts_edit'),
]
