from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    #Определение активных меню для основного URL
    menu_name1 = 'Автомобили'
    menu_name2 = 'Мотоциклы'
    return render(request, 'main/index.html', {'menu_name1': menu_name1, 'menu_name2': menu_name2})



