from django.conf.urls import url
from ..views import introduction

urlpatterns = [
    url(r'^save$', introduction.save, name='introduction_save'),
]