from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from app.models import Post
from users.models import CustomUser


class ProfileUserView(DetailView):

    model = CustomUser
    template_name = "app/profile.html"

    def get_object(self, queryset=None):
        user_id = self.kwargs.get("profile_id")
        queryset = get_object_or_404(CustomUser, id=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        posts = (
            Post.objects.filter(user=self.object)
            .annotate(
                likes_amount=Count("likes", distinct=True),
                comments_amount=Count("comments", distinct=True),
            )
            .select_related("user")
            .order_by("-created_at")
        )

        context["posts"] = posts
        return context
