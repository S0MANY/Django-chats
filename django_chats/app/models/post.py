from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin
from utils.snowflake_helper import get_snowflake_id


class Post(TimeStampMixin):

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "Посты"

    id = models.BigIntegerField(
        primary_key=True, editable=False, default=get_snowflake_id
    )

    text = models.TextField(null=False)
    user = models.ForeignKey(
        to="users.CustomUser", on_delete=models.CASCADE, related_name="posts"
    )
    likes = models.ManyToManyField(
        "users.CustomUser", related_name="liked_posts", blank=True
    )

    def __str__(self):
        return f"{self.user.username} | {self.text[:20]}..."
