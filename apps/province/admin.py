from django.contrib import admin
from .models import Province


class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('province', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('province', 'is_active',),
        }),
    )


admin.site.register(Province, ProvinceAdmin)
