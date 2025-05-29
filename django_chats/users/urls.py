from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from users.views import *

app_name = "users"

urlpatterns = [
    path("sign-in/", CustomLoginView.as_view(), name="login"),
    path("sign-up/", CustomRegisterView.as_view(), name="registration"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]
    )
