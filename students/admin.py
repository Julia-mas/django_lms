from django.contrib import admin  # noqa

from students.models import Students


class StudentsAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday',
        'group',
    ]

    list_display_links = list_display
    list_per_page = 10
    search_fields = ['first_name', 'last_name']
    list_filter = ('group',)

    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        ('enroll_date', 'graduate_date'),
        'group',
    ]

    readonly_fields = ['age']


admin.site.register(Students, StudentsAdmin)

