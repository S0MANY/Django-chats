from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from chats.models import Chat, ChatMember
from users.models import CustomUser


def start_chat(request, user_id):

    user = request.user
    target_user_id = user_id
    target_user = get_object_or_404(CustomUser, id=target_user_id)

    chat = (
        Chat.objects.filter(is_group=False, chat_members__user=user)
        .filter(chat_members__user=target_user)
        .distinct()
        .first()
    )

    if not chat:
        chat = Chat.objects.create(is_group=False)
        ChatMember.objects.bulk_create(
            [
                ChatMember(chat=chat, user=user),
                ChatMember(chat=chat, user=target_user),
            ]
        )

        return HttpResponseRedirect(
            reverse_lazy("chats:chat_details", kwargs={"chat_id": chat.id})
        )

    return HttpResponseRedirect(
        reverse_lazy("chats:chat_details", kwargs={"chat_id": chat.id})
    )
