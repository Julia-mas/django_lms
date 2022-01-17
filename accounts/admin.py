from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Profile


class ProfileInlineAdmin(admin.StackedInline):
    width = 200
    model = Profile
    can_delete = False
    fields = [
        'user',
        ('avatar', 'av_image_1'),
        'birthday',
        'city'
    ]
    readonly_fields = ['av_image_1']

    def av_image_1(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="{self.width}" />')

    av_image_1.short_description = 'Your avatar'


class CustomUserAdmin(UserAdmin):
    width = 100
    inlines = [ProfileInlineAdmin]
    list_display = ['username', 'email', 'is_staff', 'av_image']
    fieldsets = (
        (None, {'fields': (('username', 'email'), 'password')}),
        ('Personal info', {'fields': (('first_name', 'last_name'),)}),
        ('Permissions', {
            'fields': (('is_active', 'is_staff', 'is_superuser'), 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': (('last_login', 'date_joined'),)}),
    )
    readonly_fields = ['last_login', 'date_joined']

    def av_image(self, obj):
        return mark_safe(f'<img src="{obj.profile.avatar.url}" width="{self.width}" />')

    av_image.short_description = 'Avatar'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
