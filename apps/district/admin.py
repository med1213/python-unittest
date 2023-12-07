from django.contrib import admin
from .models import District


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('province', 'district', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('province', 'district', 'is_active',),
        }),
    )


admin.site.register(District, DistrictAdmin)