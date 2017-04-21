from django.conf.urls import url
from ..views import page18

urlpatterns = [
    url(r'^$', page18.init, name='page18_init'),
    url(r'^init$', page18.init, name='page18_init'),
    url(r'^(?P<pk>\d+|None)$', page18.edit, name='page18_edit'),
]