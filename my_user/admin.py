from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_staff', 'is_superuser']

    class Meta:
        model = UserProfile


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)
