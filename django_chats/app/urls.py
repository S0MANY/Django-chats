from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from app.views import *

app_name = "app"

urlpatterns = [
    path("", IndexView.as_view(), name="homepage"),
    path("write-post/", CreatePostView.as_view(), name="write_post"),
    path("post/<int:post_id>/like/", toggle_reaction, name="toggle_reaction"),
    path("post/<int:post_id>/comments/", CommentsView.as_view(), name="post_comments"),
    path("edit-post/<int:post_id>/", UpdatePostView.as_view(), name="edit_post"),
    path("profile/<int:profile_id>/", ProfileUserView.as_view(), name="profile"),
    path(
        "edit-profile/<int:profile_id>/",
        UpdateProfileView.as_view(),
        name="edit_profile",
    ),
    path("users/", UsersListView.as_view(), name="users"),
    path("tasks/", TaskListView.as_view(), name="tasks"),
    path("task/<int:task_id>", TaskDetailView.as_view(), name="task_detail"),
    path("edit-task/<int:task_id>", change_task_status, name="edit_task"),
    path("profile/logout/", logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
