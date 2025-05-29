from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin


class Messages(TimeStampMixin):

    chat = models.ForeignKey("Chat", on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    text = models.TextField(null=False)
