from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category, Post
from datetime import datetime


class Homeview(View):
    def get(self, request):
        category_list = Category.objects.all()
        posts = Post.objects.filter(published_date__lte=datetime.now(), published=True,)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'posts': posts})


class CategoryView(View):
    """Вывод статей категории"""

    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})


class PostDetailView(View):
    """Вывод полной статьи"""

    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {'categories': category_list, 'post': post})
