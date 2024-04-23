#ARFood/views.py
from django.shortcuts import render
from .models import Food

def menu(request):
    foods = Food.objects.all()
    return render(request, 'menu.html', {'foods': foods})

def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'food_detail.html', {'food': food})
