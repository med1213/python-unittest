from django.contrib import admin
from .models import Bill


class BillAdmin(admin.ModelAdmin):

    list_display = ('is_draw', 'total_cost',
                    'device_number', 'bill_number', 'candidate', "image", 'is_active', )
    fieldsets = (
        (None, {
            'fields': ('period', 'is_draw', 'total_cost',
                       'device_number', 'bill_number', 'candidate', "image", 'is_active', )
        }),
    )


admin.site.register(Bill, BillAdmin)
