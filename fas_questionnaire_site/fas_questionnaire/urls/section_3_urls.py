from django.conf.urls import url
from ..views import section_3_view

urlpatterns = [
    url(r'^new$', section_3_view.new, name='section_3_view_new'),
    url(r'^(?P<pk>\d+)/update$', section_3_view.update, name='section_3_view_update'),
    url(r'^get$', section_3_view.get, name='section_3_view_get'),
]