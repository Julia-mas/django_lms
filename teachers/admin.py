from django.contrib import admin # noqa

from teachers.models import Teachers


class TeacherAdmin(admin.ModelAdmin):

    list_display = [
        'first_name',
        'last_name',
        'birthday',
        'age',
        'seniority_years',
        'phone_number'
    ]
    list_display_links = list_display

    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'seniority_years',
        'phone_number',
        'group'
    ]
    readonly_fields = ['age']
    list_per_page = 10
    search_fields = ['first_name', 'last_name']
    list_filter = ('group',)


admin.site.register(Teachers, TeacherAdmin)
