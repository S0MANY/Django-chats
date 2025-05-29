from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from app.models import Task


class TaskDetailView(DetailView):

    model = Task
    template_name = "app/task_detail.html"

    def get_object(self, queryset=None):
        task_id = self.kwargs.get("task_id")
        queryset = get_object_or_404(Task, id=task_id, user=self.request.user)
        return queryset

