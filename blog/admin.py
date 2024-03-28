from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_published', 'is_active',)
    list_filter = ('title', 'content', 'views_count', 'date_published', 'is_active',)
    