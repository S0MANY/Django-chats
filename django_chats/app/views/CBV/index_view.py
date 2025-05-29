from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import ListView

from app.models import Post


class IndexView(LoginRequiredMixin, ListView):

    template_name = "app/index.html"
    model = Post

    def get_queryset(self):

        posts = (
            Post.objects.all()
            .annotate(
                likes_amount=Count("likes", distinct=True),
                comments_amount=Count("comments", distinct=True),
            )
            .select_related("user")
            .order_by("-created_at")
        )

        queryset = []

        for post in posts:
            queryset.append(
                {
                    "id": post.id,
                    "author": post.user,
                    "full_name": post.user.get_full_name,
                    "text": post.text,
                    "likes_amount": post.likes_amount,
                    "comments_amount": post.comments_amount,
                }
            )

        return queryset
