from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('period', 'title', 'sub_title', 'description', 'phone', 'address', 'image','is_active', )
    fieldsets = (
        (None, {
            'fields': ('period', 'title', 'sub_title', 'description', 'phone', 'address', 'image','is_active',),
        }),
    )


admin.site.register(Post, PostAdmin)