from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category


# Create your views here.

# def home(request):
#     if request.method == "POST":
#         return HttpResponse('Hi')
#     elif request.method == "GET":
#         return HttpResponse("good")


class Homeview(View):
    def get(self, request):
        category_list = Category.objects.all()
        return render(request, 'blog/home.html', {'categories': category_list})


class CategoryView(View):
    """Вывод статей категории"""

    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})
