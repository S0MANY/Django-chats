from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from app.models import Task


@require_POST
def change_task_status(request, task_id):

    new_status = request.POST.get("status")
    task = get_object_or_404(Task, user=request.user, id=task_id)

    if new_status in ["0", "1", "2"]:
        task.status = new_status
        task.save()

    return redirect(request.META.get("HTTP_REFERER", "app:tasks"))
