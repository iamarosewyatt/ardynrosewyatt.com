from django.contrib import admin
from journal.models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('modified', 'slug')

admin.site.register(Post, PostAdmin)
