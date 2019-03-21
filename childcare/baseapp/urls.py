from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('explore_grid/', views.explore_grid, name='explore_grid'),
    path('explore_list/', views.explore_list, name='explore_list'),
    path('subsidy/', views.subsidy, name='subsidy'),
    path('maps/', views.maps, name='maps' )
]