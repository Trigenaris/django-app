from django.contrib import admin
from .models import Article, Comment, FooterSettings, Service

# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_date", "is_approved"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title", "is_approved"]
    list_filter = ["created_date", "is_approved"]
    class Meta:
        model = Article

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username')

admin.site.register(FooterSettings)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title',)
    readonly_fields = ('created_date',)