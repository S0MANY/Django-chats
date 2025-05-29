from django.db import models

from utils.database.mixins.timestam_mixins import TimeStampMixin


class Task(TimeStampMixin):

    class TaskStatus(models.IntegerChoices):

        IN_PROGRESS = 0, "В процессе"
        DONE = 1, "Готово"
        FAILED = 2, "Не выполнено"

    name = models.CharField(max_length=256, null=False)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.IntegerField(choices=TaskStatus, default=TaskStatus.IN_PROGRESS)
    user = models.ForeignKey(
        to="users.CustomUser", on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return f"{self.user.username} | {self.name} ({self.get_status_display()})"
