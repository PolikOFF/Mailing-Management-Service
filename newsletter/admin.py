from django.contrib import admin

from newsletter.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'email', 'comments')
    list_filter = ('fio', )
    search_fields = ('fio', )
