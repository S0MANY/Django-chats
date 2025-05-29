from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from app.forms import CreateCommentForm
from app.models import Comment, Post


class CommentsView(CreateView):

    model = Comment
    template_name = "app/comments.html"
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        comment_list = (
            Comment.objects.filter(post=post)
            .select_related("user")
            .order_by("-created_at")
        )

        context["comments"] = comment_list
        context["post"] = post

        return context

    def form_valid(self, form):
        data = form.cleaned_data
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        Comment.objects.create(
            text=data["text"],
            user=self.request.user,
            post=post,
        )

        return redirect(self.request.META.get("HTTP_REFERER", "app:homepage"))
