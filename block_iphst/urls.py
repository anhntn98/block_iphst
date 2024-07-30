from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import  views


urlpatterns = [
    path('add/'.views.add.as_view(),name='add'),
    path('remove/'.views.add.as_view(),name='remove')
    path('', views.BlockIP.as_view(), name='BlockIp'),
]

