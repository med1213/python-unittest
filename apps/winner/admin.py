from django.contrib import admin
from .models import Winner


class WinnerAdmin(admin.ModelAdmin):
    list_display = ('prize', 'lottery_bill', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('prize', 'lottery_bill', 'is_active',),
        }),
    )


admin.site.register(Winner, WinnerAdmin)
