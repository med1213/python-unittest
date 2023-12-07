from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'is_active',
                    'province', 'district', 'village')
    fieldsets = (
        (None, {
            'fields': ('full_name', 'phone_number', 'is_active',
                       'province', 'district', 'village'),
        }),
    )


admin.site.register(Candidate, CandidateAdmin)
