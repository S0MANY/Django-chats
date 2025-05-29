from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

from chats.models import Chat
from django_chats import settings
from utils.image_rename import rename_uploaded_file
from utils.snowflake_helper import get_snowflake_id


class CustomUser(AbstractUser):

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"

    id = models.BigIntegerField(
        primary_key=True, editable=False, default=get_snowflake_id
    )

    user_image = models.ImageField(
        upload_to=rename_uploaded_file, null=True, blank=True
    )
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.user_image and self.user_image.name:
            try:
                image_path = self.user_image.path
                img = Image.open(fp=image_path)
                max_size = (300, 300)
                img.thumbnail(size=max_size)
                img.save(image_path)
            except Exception as e:
                print(f"Ошибка при ресайзе изображения: {e}")

    @property
    def get_full_name(self):
        if self.last_name and self.first_name:
            return f"{self.last_name} {self.first_name}"
        else:
            return self.username

    @property
    def get_user_image_url(self):
        if self.user_image and self.user_image.name:
            try:
                if self.user_image.storage.exists(self.user_image.name):
                    return self.user_image.url
            except Exception as e:
                pass
        return settings.STATIC_URL + "img/default_image.png"
