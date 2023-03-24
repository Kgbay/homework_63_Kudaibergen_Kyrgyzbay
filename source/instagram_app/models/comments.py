from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Comment(models.Model):
    text = models.TextField(
        max_length=3000,
        null=False,
        verbose_name="Описание поста"
    )
    user = models.ForeignKey(
        to=User,
        related_name='comment_user',
        verbose_name='Пользователь',
        null=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        'instagram_app.Post',
        related_name='post',
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Пост',
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