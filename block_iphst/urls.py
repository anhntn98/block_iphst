from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import  views


urlpatterns = [
    path('', views.BlockIP.as_view(), name='BlockIp'),
]

