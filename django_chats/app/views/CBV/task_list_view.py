from django.views.generic import ListView

from app.models import Task


class TaskListView(ListView):

    model = Task
    template_name = "app/task_list.html"

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        return queryset
