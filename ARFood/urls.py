# ARFood/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
]
