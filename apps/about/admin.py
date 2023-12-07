from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'image', 'is_active',),
        }),
    )


admin.site.register(About, AboutAdmin)