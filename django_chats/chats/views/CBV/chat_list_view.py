from django.views.generic import ListView

from chats.models import Chat, Messages


class ChatListView(ListView):

    model = Chat
    template_name = "chats/chat_list.html"

    def get_queryset(self):
        chats = Chat.objects.filter(chat_members__user=self.request.user)
        queryset = []

        for chat in chats:

            last_message = chat.messages.last()

            chat_data = {
                "id": chat.id,
                "is_group": chat.is_group,
                "last_message": last_message.text if last_message else None,
                "last_sender": last_message.sender.get_full_name if last_message.sender else "no-name",
            }

            if chat.is_group:
                chat_data.update({"title": chat.title})
            else:
                members = chat.chat_members.all()
                print(members)
                chat_with = [member for member in members if member.user != self.request.user][0].user

                chat_data.update({"chat_with": chat_with})

            queryset.append(chat_data)

        return queryset
