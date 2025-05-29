from django import forms

from app.models import Comment


class CreateCommentForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full border border-gray-300 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none bg-white",
                "placeholder": "Ваш комментарий.",
            }
        )
    )

    class Meta:
        model = Comment
        fields = ["text"]
