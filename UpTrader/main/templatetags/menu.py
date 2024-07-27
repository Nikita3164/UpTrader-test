from django import template
from django.shortcuts import render
from main.models import Menu
from django.template.loader import get_template

register = template.Library()

@register.inclusion_tag("main/menu.html")
def draw_menu(menu_name):
    menu = Menu.objects.filter(menu_name__contains=menu_name)
    lvl_1 = []
    lvl_2 = {}
    for i in menu:
        if i.lvl_1 not in lvl_1:
            lvl_1.append(i.lvl_1)
        print(menu_name)
        if lvl_2.get(i.lvl_1) == None:
           lvl_2[i.lvl_1] = []
        lvl_2[i.lvl_1].append([i.lvl_2, i.lvl_2_ref])   
    return {"menu_name": menu_name, "lvl_1": lvl_1, "lvl_2": lvl_2}