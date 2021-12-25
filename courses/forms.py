from django import forms
from django_filters import FilterSet

from .models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('start_date',)


class CoursesFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'name': ['exact'],
            'start_date': ['exact', 'month__gt'],
            'group': ['exact'],
        }
        widgets = {'start_date': forms.DateInput(attrs={'type': 'date'})}


class CourseUpdateForm(CourseCreateForm):
    class Meta(CourseCreateForm.Meta):
        model = Course
        exclude = ('start_date',)
        