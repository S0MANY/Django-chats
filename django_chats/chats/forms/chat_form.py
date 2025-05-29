from django import forms

from chats.models import Messages


class MessageForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "flex-1 border rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400",
                "placeholder": "Напишите сообщение...",
                "type": "text",
                "autocomplete": "off",
            }
        )
    )

    class Meta:
        model = Messages
        fields = ["text"]
