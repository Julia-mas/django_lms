from django.contrib import admin # noqa

from groups.models import Groups
from students.models import Students


class StudentsInlineTable(admin.TabularInline):
    model = Students
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number',
    ]
    extra = 0
    # readonly_fields = fields
    # show_change_link = True


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'groups_name',
        'groups_country',
        'groups_language',
        'members_qty',
        'headman'
    ]
    list_display_links = list_display

    fields = [
        'groups_name',
        ('groups_country','groups_language'),
        'members_qty',
        'headman',
        'teachers',
    ]

    inlines = [StudentsInlineTable]


admin.site.register(Groups, GroupAdmin)
