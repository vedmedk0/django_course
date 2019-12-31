from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from django.utils import timezone
from django.urls import reverse


# Create your models here.

class Category(MPTTModel):
    """Модель категории"""
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)  # то что хранится по url
    description = models.TextField('Описание', max_length=1000, default='', blank=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    template = models.CharField('Шаблон', max_length=500, default='blog/post_list.html')
    published = models.BooleanField('Отображать', default=True)
    paginated = models.PositiveIntegerField('Количество новостей на странце', default=5)
    sort = models.PositiveIntegerField('Порядок', default=0)

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

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    """Модель поста"""
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=100, blank=True, null=True)
    mini_text = models.TextField(verbose_name="Краткое содержание", max_length=300)
    text = models.TextField(verbose_name="Текст")
    created_date = models.DateTimeField(verbose_name="Дата создания")
    slug = models.SlugField(verbose_name='url', max_length=100)
    category = models.ForeignKey(Category,
                                 verbose_name="Категория",
                                 on_delete=models.CASCADE,
                                 null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тег', blank=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    edit_date = models.DateTimeField(
        'Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        blank=True,
        null=True
    )
    image = models.ImageField('Главная фотография', upload_to='post/', null=True, blank=True)
    template = models.CharField('Шаблон', max_length=500, default='blog/post_details.html')
    viewed = models.PositiveIntegerField('Просмотрено', default=0)
    status = models.BooleanField('Для зарегистрированных', default=False)
    sort = models.PositiveIntegerField('Порядок', default=0)
    published = models.BooleanField('Отображать', default=True)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category': self.category.slug, 'slug': self.slug})

    def __str__(self):
        return self.title

    def render_tags(self):
        return ', '.join([tag.name for tag in self.tags.all()])

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    """Модель комментария"""
    author = models.ForeignKey(User,
                               verbose_name="Автор",
                               on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст")
    creation_date = models.DateTimeField(verbose_name="Дата создания")
    moderation = models.BooleanField(verbose_name="Модерация")
    post = models.ForeignKey(Post, verbose_name='Статья', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"
