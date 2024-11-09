from django.contrib import admin
from .models import Contact, About

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_display_links = ["name", "email"]
    search_fields = ["name", "email"]
    list_filter = ["created_at"]

admin.site.register(About)