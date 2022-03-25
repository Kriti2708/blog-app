from django.contrib import admin
from .models import Post, Comment, Category, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Profile)
