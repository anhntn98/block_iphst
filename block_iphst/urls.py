from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import  views

app_name = 'block_iphst'
urlpatterns = [
    path('add/', views.Add_Block.as_view(),name='add'),
    path('remove/', views.Remove_Block.as_view(),name='remove'),
    path('', views.BlockIP.as_view(), name='BlockIp'),
]

