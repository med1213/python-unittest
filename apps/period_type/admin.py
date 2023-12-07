from django.contrib import admin
from .models import PeriodType


class PeriodTypeAdmin(admin.ModelAdmin):
    list_display = ('period_type', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('period_type', 'is_active',),
        }),
    )


admin.site.register(PeriodType, PeriodTypeAdmin)
