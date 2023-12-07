from django.contrib import admin
from .models import Prize


class PrizeAdmin(admin.ModelAdmin):
    list_display = ('prize_type', 'prize', 'quantity', 'detail', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('prize_type', 'prize', 'quantity',  'detail', 'is_active',),
        }),
    )


admin.site.register(Prize, PrizeAdmin)
