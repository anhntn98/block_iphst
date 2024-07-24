from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from . import models, views


urlpatterns = (
    path('', views.BlockIP.as_view(), name='BlockIP')
)

