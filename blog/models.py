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
