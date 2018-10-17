from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.pools, name='pools'),
    path('', views.home_view, name='home_view'),
]
