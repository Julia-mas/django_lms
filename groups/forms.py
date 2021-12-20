from django import forms
from django_filters import FilterSet

from .models import Groups


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = [
            'groups_name',
            'groups_nationality',
            'groups_language',
            'members_qty'
        ]


class GroupsFilter(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'members_qty': ['lt', 'gt'],
            'groups_name': ['exact', 'startswith'],
        }


class GroupUpdateForm(GroupCreateForm):
    class Meta(GroupCreateForm.Meta):
        fields = '__all__'
