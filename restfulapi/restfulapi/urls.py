from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from addresses import views

urlpatterns = [
    path(r'addresses/', views.address_list),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
