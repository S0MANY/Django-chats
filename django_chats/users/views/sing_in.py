from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.forms import CustomLoginForm


class CustomLoginView(LoginView):

    template_name = "users/login.html"
    form_class = CustomLoginForm
    success_url = reverse_lazy("app:homepage")
