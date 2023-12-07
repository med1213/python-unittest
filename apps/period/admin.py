from django.contrib import admin
from .models import Period


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('period', 'open_date', 'close_date', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('period', 'open_date', 'close_date', 'is_active',)
        }),
    )


admin.site.register(Period, PeriodAdmin)
