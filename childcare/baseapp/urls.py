from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='Homepage'),
    path('explore_grid/', views.explore_grid, name='Explore_Grid'),
    path('explore_list/', views.explore_list, name='Explore_List'),
    path('subsidy/', views.subsidy, name='subsidy'),
]