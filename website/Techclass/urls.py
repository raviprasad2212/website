from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.Course, name='Home-page'),
]
