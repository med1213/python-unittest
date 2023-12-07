from django.contrib import admin
from .models import PrizeType


class PrizeTypeAdmin(admin.ModelAdmin):
    list_display = ('prize_type', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('prize_type', 'is_active',),
        }),
    )


admin.site.register(PrizeType, PrizeTypeAdmin)
