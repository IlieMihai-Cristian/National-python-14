from django.urls import include, path
from rest_framework import routers

from myapi import views

router = routers.DefaultRouter()
router.register('location', views.LocationViewSet)

urlpatterns = [
    path('', include(router.urls))
]