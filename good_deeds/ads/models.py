from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        unique=True,
        db_index=True,
        max_length=200
    )
    slug = models.SlugField(
        'Ссылка',
        unique=True,
        max_length=200
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Название объявления'
    )
    description = models.TextField(
        verbose_name='Описание объявления'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время публикации'
    )
    image = models.ImageField(
        upload_to='ads/images/',
        verbose_name='Изображение вещи'
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class AdRequest(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время отклика'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.user} подал заявку на {self.ad.title}'


class ApplicantList(models.Model):
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    is_selected = models.BooleanField(
        default=False,
        verbose_name='Выбор кандидата'
    )

    class Meta:
        verbose_name = 'Список претендентов'
