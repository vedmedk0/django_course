from django.db import models


# Create your models here.

class Category(models.Model):
    """Модель категории"""
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)  # то что хранится по url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Tag(models.Model):
    """Модель тега"""
    name = models.CharField(verbose_name="Название тега", max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)  # то что хранится по url

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель поста"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    mini_text = models.TextField(verbose_name="Summary", max_length=300)
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(verbose_name="Дата создания")
    slug = models.SlugField(verbose_name='url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Comment(models.Model):
    """Модель комментария"""
    text = models.TextField(verbose_name="Текст")
    creation_date = models.DateTimeField(verbose_name="Дата создания")
    moderation = models.BooleanField(verbose_name="Модерация")

    def __str__(self):
        return self.text
