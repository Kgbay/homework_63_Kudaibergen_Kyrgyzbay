from django.contrib import admin

from django.contrib import admin
from .models import Comment, Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'post', 'created_at')
    list_filter = ('id', 'text', 'created_at')
    search_fields = ('text', 'post', 'user')
    fields = ('text', 'post', 'user')
    readonly_fields = ('id', 'updated_at')


admin.site.register(Comment, CommentAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('desc', 'image', 'user', 'likes_count', 'location', 'created_at')
    list_filter = ('user', 'location', 'created_at', 'updated_at')
    search_fields = ('user', 'location', 'created_at', 'updated_at')
    fields = ('desc', 'image', 'point', 'location', 'user',)


admin.site.register(Post, PostAdmin)
