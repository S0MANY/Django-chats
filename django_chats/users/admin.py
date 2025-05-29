from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, format_html_join

from users.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        "username",
        "is_active",
        "created_at",
    ]

    search_fields = [
        "username",
        "is_active",
        "created_at",
    ]

    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_superuser",
        "is_active",
        "groups",
        "user_permissions",
    ]

    readonly_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
    ]





