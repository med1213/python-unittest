from django.contrib import admin

# Register your models here.
from .models import LiveData

class LiveDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status',)
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'status',),
        }),
    )


admin.site.register(LiveData, LiveDataAdmin)