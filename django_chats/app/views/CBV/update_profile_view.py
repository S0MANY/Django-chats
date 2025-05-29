from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from app.forms import CustomUserChangeForm
from users.models import CustomUser


class UpdateProfileView(UpdateView):

    model = CustomUser
    template_name = "app/edit_profile.html"
    form_class = CustomUserChangeForm

    def get_object(self, queryset=None):
        profile_id = self.kwargs.get("profile_id")
        profile = get_object_or_404(CustomUser, id=profile_id)

        if profile != self.request.user:
            return HttpResponseForbidden(reverse_lazy("app:homepage"))

        return profile

    def get_success_url(self):
        return reverse_lazy("app:profile", kwargs={"profile_id": self.object.id})
