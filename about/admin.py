from about.models import Moment
from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin


class MomentAdmin(OrderedModelAdmin):
    readonly_fields = ('order', 'created', 'modified')
    list_display = ('move_up_down_links', 'when', 'what')
    list_display_links = ('when', 'what')

    class Media:
        css = {'all': ('admin.css',)}


admin.site.register(Moment, MomentAdmin)
