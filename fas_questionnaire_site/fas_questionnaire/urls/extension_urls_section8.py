from django.conf.urls import url
from ..views import source_and_type_of_extension_services_section8 as extension

urlpatterns = [
    url(r'^$', extension.new, name='extension_new'),
    url(r'^init$', extension.init, name='extension_init'),
    url(r'^(?P<pk>\d+|None)$', extension.edit, name='extension_edit'),
    url(r'^get$', extension.get, name='extension_get'),
]