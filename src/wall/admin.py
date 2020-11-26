from django.contrib import admin
from .models import Comment, Post
from mptt.admin import MPTTModelAdmin


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """комментарии к посту"""

    list_display = ('user', 'published', 'create_date', 'moderation', 'view_count', 'id')


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin, admin.ModelAdmin):
    """комментарии к посту"""
    list_display = ('user', 'post',)
    mptt_level_indent = 15