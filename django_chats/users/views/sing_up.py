from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CustomRegisterForm


class CustomRegisterView(CreateView):

    template_name = "users/register.html"
    form_class = CustomRegisterForm
    success_url = reverse_lazy("enter:login")
