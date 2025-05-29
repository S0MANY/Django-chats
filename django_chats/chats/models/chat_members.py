from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin


class ChatMember(TimeStampMixin):

    chat = models.ForeignKey(
        "Chat", on_delete=models.CASCADE, related_name="chat_members"
    )

    user = models.ForeignKey(
        "users.CustomUser", on_delete=models.CASCADE, related_name="user_chats"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("chat", "user")
