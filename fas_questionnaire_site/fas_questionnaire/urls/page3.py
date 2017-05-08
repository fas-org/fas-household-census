from django.conf.urls import url
from ..views import page3 as page3

urlpatterns = [
    url(r'^$', page3.init, name='page3_init'),
    url(r'^init$', page3.init, name='page3_init'),
    url(r'^(?P<pk>\d+|None)$', page3.edit, name='page3_edit'),

]