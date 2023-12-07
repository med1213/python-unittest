from django.contrib import admin
from .models import Slide


class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'is_active',),
        }),
    )


admin.site.register(Slide, SlideAdmin)