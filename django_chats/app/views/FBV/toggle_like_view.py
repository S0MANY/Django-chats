from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from app.models import Post


def toggle_reaction(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return HttpResponseRedirect(
        redirect_to=request.META.get("HTTP_REFERER", "app:homepage")
    )
