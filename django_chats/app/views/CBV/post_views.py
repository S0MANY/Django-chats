from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from app.forms import CreatePostForm
from app.models import Post


class CreatePostView(CreateView):

    template_name = "app/create_post.html"
    model = Post
    form_class = CreatePostForm

    def form_valid(self, form):
        data = form.cleaned_data

        Post.objects.create(text=data["text"], user=self.request.user)

        return redirect("app:homepage")


class UpdatePostView(UpdateView):

    template_name = "app/update_post.html"
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy("app:homepage")

    def get_object(self, queryset=None):

        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, id=post_id)

        if post.user != self.request.user:
            raise PermissionDenied("Not allowed")

        return post
