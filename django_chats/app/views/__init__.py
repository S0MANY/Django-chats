__all__ = [
    "IndexView",
    "CreatePostView",
    "UpdatePostView",
    "CommentsView",
    "ProfileUserView",
    "UsersListView",
    "TaskListView",
    "UpdateProfileView",
    "TaskDetailView",
    "toggle_reaction",
    "logout_view",
    "change_task_status",
]

from app.views.CBV.comment_views import CommentsView
from app.views.CBV.index_view import IndexView
from app.views.CBV.post_views import CreatePostView, UpdatePostView
from app.views.CBV.profile_view import ProfileUserView
from app.views.CBV.task_detail import TaskDetailView
from app.views.CBV.task_list_view import TaskListView
from app.views.CBV.update_profile_view import UpdateProfileView
from app.views.CBV.users_list_view import UsersListView
from app.views.FBV.change_task_status import change_task_status
from app.views.FBV.logout_view import logout_view
from app.views.FBV.toggle_like_view import toggle_reaction
