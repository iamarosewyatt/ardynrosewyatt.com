from about.models import Moment
from django.contrib import admin
from django.contrib.admin import ModelAdmin


class MomentAdmin(ModelAdmin):
    readonly_fields = ('created', 'modified')
    ordering = ('when',)


admin.site.register(Moment, MomentAdmin)
