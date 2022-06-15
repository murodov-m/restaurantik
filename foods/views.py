from django.shortcuts import render
from django.views.generic.base import View
from .models import Food

class FoodView(View):
    def get(self, request):
        foods = Food.objects.all()
        return render(request, 'food.html', {'foods': foods})


class FoodDetailView(View):
    def get(self, request, pk):
        food = Food.objects.get(id=pk)
        return render(request, 'food.html', {"food":food})

    # c2 = Food.objects.all()
    # context = {'obj_list': c2}
    # print(c2)
    # return render(request, 'food.html', context=context)