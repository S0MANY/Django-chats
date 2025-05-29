from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from chats.forms import MessageForm
from chats.models import Chat, Messages


class ChatDetailView(LoginRequiredMixin, FormMixin, DetailView):

    model = Chat
    template_name = "chats/chat.html"
    form_class = MessageForm

    def get_object(self, queryset=None):

        chat_id = self.kwargs.get("chat_id")
        chat = get_object_or_404(Chat, id=chat_id)

        return chat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat = Chat.objects.filter(id=self.kwargs.get("chat_id")).first()
        members = chat.chat_members.all()
        context["chat_with"] = [
            member for member in members if member.user != self.request.user
        ][0].user.get_full_name
        context["chat_messages"] = Messages.objects.filter(chat=chat)
        return context

    def form_valid(self, form):
        data = form.cleaned_data

        Messages.objects.create(
            chat=self.object,
            sender=self.request.user,
            text=data["text"],
        )
        return redirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        return self.request.path
