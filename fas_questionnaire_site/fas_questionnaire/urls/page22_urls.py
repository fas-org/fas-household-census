from django.conf.urls import url
from ..views import page22_view as page22   

urlpatterns = [
    url(r'^$', page22.edit, name='page22_edit'),
    url(r'^init$', page22.init, name='page22_init'),
    url(r'^(?P<pk>\d+|None)$', page22.edit, name='page22_edit')
]