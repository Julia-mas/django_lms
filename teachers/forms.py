from django import forms
from django_filters import FilterSet

from .models import Teachers
from .validators import normalize_phone


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_number = normalize_phone(phone_number)
        return phone_number

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self.normalize_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self.normalize_name(last_name)


class TeachersFilter(FilterSet):
    class Meta:
        model = Teachers
        fields = {
            'seniority_years': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }


class TeacherUpdateForm(TeacherCreateForm):
    class Meta(TeacherCreateForm.Meta):
        fields = '__all__'
