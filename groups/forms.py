from django import forms

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
