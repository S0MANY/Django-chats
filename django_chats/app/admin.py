from django.contrib import admin

from app.models import Comment, Post, Task

# Register your models here.


class CommentAdmin(admin.TabularInline):

    model = Comment
    readonly_fields = ["user", "text"]
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ["user__username", "brief_text", "created_at"]
    list_display_links = ["user__username", "brief_text"]

    readonly_fields = ["text", "user", "likes"]
    ordering = ["-created_at"]

    inlines = [CommentAdmin]

    def brief_text(self, obj):
        if len(obj.text) < 20:
            return obj.text
        else:
            return f"{obj.text[:20]}..."


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ["user__username", "name", "deadline"]
    list_display_links = ["user__username", "name"]
