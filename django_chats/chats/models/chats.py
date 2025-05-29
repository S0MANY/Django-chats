from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin
from utils.snowflake_helper import get_snowflake_id


class Chat(TimeStampMixin):

    class Meta:
        verbose_name = "чат"
        verbose_name_plural = "Чаты"

    id = models.BigIntegerField(
        primary_key=True, editable=False, default=get_snowflake_id
    )

    title = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=True)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return "Без названия"

    def users(self):
        members = self.chat_members.select_related("user").all()

        if len(members) == 2:
            return f"{members[0]} & {members[1]}"
        else:
            return f"{members[0]} & {members[1]} & {len(members)-2} more"
