from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class SexChoice(TextChoices):
    MALE = ('Male', 'Мужской')
    FEMALE = ('Female', 'Женский')


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Телефон номера'
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_picture',
        verbose_name='Аватар'
    )
    sex = models.CharField(
        max_length=100,
        null=False,
        choices=SexChoice.choices,
        verbose_name='Пол',
        default=SexChoice.MALE
    )
    bio = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='Биография пользователя')
    subscribers_count = models.PositiveIntegerField(
        verbose_name='Количество подписчиков',
        null=False,
        default=0
    )
    subscriptions_count = models.PositiveIntegerField(
        verbose_name='Количество подписок',
        null=False,
        default=0
    )
    publications_count = models.PositiveIntegerField(
        verbose_name='Количество публикации',
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

    def __str__(self):
        return f"{self.user}, {self.birth_date}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
