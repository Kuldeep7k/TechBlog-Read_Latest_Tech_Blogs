from django.contrib import admin
from .models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author',)
    list_filter = ('author', 'tags',)
    search_fields = ('title', 'content',)
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'text', 'post',)


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
