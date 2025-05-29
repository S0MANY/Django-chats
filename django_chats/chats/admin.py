from django.contrib import admin

from chats.models import Chat, ChatMember, Messages


class MessagesAdmin(admin.TabularInline):

    model = Messages
    readonly_fields = ["sender", "text"]

    extra = 0


class ChatMemberAdmin(admin.StackedInline):

    model = ChatMember
    readonly_fields = ["user"]
    extra = 0


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):

    list_display = ["id", "users", "title", "is_group", "created_at"]

    list_display_links = [
        "id",
        "users",
    ]

    search_fields = [
        "chat_members__user__username",
        "chat_members__user__first_name",
        "chat_members__user__last_name",
        "chat_members__user__email",
        "title",
    ]

    inlines = [ChatMemberAdmin, MessagesAdmin]
