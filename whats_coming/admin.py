from django.contrib import admin
from whats_coming.model import Item


class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')


admin.site.register(Item, ItemAdmin)
