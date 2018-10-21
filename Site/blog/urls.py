from django import views
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.pools, name='blog'),
    path('', views.home_view, name='home_view'),
    url('', views.index, name='index'),
    url(r'^post/$',views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post_details, name='post_details'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$',views.post_comment, name='post_comment'),
    url(r'^post/(?P<pk>[0-9]+)/comment/add_comment/$',views.add_comment, name='add_comment'),
]
