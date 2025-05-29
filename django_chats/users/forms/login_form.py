from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Логин",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Пароль",
            }
        )
    )
