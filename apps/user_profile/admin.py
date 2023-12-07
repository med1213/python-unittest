from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'first_name', 'last_name', "gender", "profile_pic", "phone_number", 'is_active',)
    fieldsets = (
        (None, {
            'fields': ('owner', 'first_name', 'last_name', "gender", "profile_pic", "phone_number", 'is_active',),
        }),
    )


admin.site.register(UserProfile, UserProfileAdmin)