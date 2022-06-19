from django import views
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *
  
# define the router
router = routers.DefaultRouter()
  
# define the router path and viewset to be used
router.register(r'geeks', GeeksViewSet)

urlpatterns = [
    path('course/', views.Course, name='Home-page'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
