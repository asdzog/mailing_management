from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_filter = ('title', 'content', 'views_count', 'date_published', 'is_active',)
    