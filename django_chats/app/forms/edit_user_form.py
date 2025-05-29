from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models import CustomUser


class CustomUserChangeForm(UserChangeForm):

    user_image = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "text-sm text-gray-600"})
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "w-full border rounded p-2 focus:ring focus:ring-blue-300"}
        ),
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "w-full border rounded p-2 focus:ring focus:ring-blue-300"}
        ),
    )

    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "w-full border rounded p-2 focus:ring focus:ring-blue-300"}
        ),
    )

    email = forms.CharField(
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "w-full border rounded p-2 focus:ring focus:ring-blue-300"}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("user_image", "first_name", "last_name", "phone", "email")
