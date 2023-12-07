from django.contrib import admin
from .models import Footer


class FooterAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'instagram_url', 'whatsapp', 'facebook_url', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('address', 'email', 'instagram_url', 'whatsapp', 'facebook_url', 'is_active',),
        }),
    )


admin.site.register(Footer, FooterAdmin)