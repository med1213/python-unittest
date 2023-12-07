from django.contrib import admin
from .models import Village


class VillageAdmin(admin.ModelAdmin):
    list_display = ('district', 'village', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('district', 'village', 'is_active',),
        }),
    )


admin.site.register(Village, VillageAdmin)