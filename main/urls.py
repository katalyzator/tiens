from django.conf.urls import url

from main.views import *

urlpatterns = [
    url(r'^$', index_view, name='index_view')
]

