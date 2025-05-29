from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from chats.views import *

app_name = "chats"

urlpatterns = [
    path("start/<int:user_id>", start_chat, name="start_chat"),
    path("<int:chat_id>/", ChatDetailView.as_view(), name="chat_details"),
    path("all/", ChatListView.as_view(), name="chats_all"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
