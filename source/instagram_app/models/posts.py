from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField

class Post(models.Model):
    desc = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Описание поста"
    )
    image = models.ImageField(
        null=False,
        upload_to='user_picture/',
        verbose_name='Изображения'
    )
    point = models.CharField(
        max_length=255,
        verbose_name='Местоположения'
    )
    location = PlainLocationField(
        based_fields=['point'],
        zoom=7
        )
    user = models.ForeignKey(
        to=User,
        related_name='posts',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE
    )
    likes_count = models.PositiveIntegerField(
        verbose_name='Количество лайков',
        null=False,
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создание"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=True,
        default=False)
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        null=True, default=None)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
