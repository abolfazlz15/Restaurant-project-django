from django.contrib import admin
from .models import Article, Tag, Category, Comment


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created')
    list_filter = ('created', 'status', 'author')
    search_fields = ('title', 'body')
    ordering = ('status',)
    list_editable = ('status',)
    list_display_links = ('title', 'author',)
