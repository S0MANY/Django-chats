from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin
from utils.snowflake_helper import get_snowflake_id


class Comment(TimeStampMixin):

    id = models.BigIntegerField(
        primary_key=True,
        editable=False,
        default=get_snowflake_id
    )

    text = models.TextField(null=False)
    user = models.ForeignKey(to="users.CustomUser", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(to="app.Post", on_delete=models.CASCADE, related_name="comments")