from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from users.models import CustomUser

phone_validator = RegexValidator(
    regex=r"^\+7 \(\d{3}\) \d{3}-\d{2}-\d{2}$",
    message="Телефон должен быть в формате +7 (XXX) XXX-XX-XX",
)


class CustomRegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Логин",
                "type": "text",
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Почта",
                "type": "email",
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Ваше имя",
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Ваша Фамилия",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Введите пароль",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 px-3 py-2 rounded focus:ring focus:ring-blue-300",
                "placeholder": "Подтвердите пароль",
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
