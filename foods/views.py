from django.shortcuts import render
from .models import FoodMenu


def menuView(request):
    foods = FoodMenu.objects.filter(status=True)
    context = {
        'foods':foods
    }
    return render(request, 'foods/menu.html', context)