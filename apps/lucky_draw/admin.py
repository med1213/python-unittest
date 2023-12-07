from django.contrib import admin
from .models import LuckyDraw


class LuckyDrawAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('item_name', 'is_active',)
        }),
    )


admin.site.register(LuckyDraw, LuckyDrawAdmin)
