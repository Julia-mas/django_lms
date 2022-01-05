from django.forms import ChoiceField, ModelForm
from django_filters import FilterSet

from .models import Groups


class GroupBaseForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = ['headman']


class GroupsFilter(FilterSet):
    class Meta:
        model = Groups
        fields = {
            'members_qty': ['lt', 'gt'],
            'groups_name': ['exact', 'startswith'],
        }


class GroupUpdateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['headman_field'] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.students.all()],
            label='Headman',
            required=False
        )
        self.fields['teachers_field'] = ChoiceField(
            choices=[(st.id, str(st)) for st in self.instance.teachers.all()],
            label='Teachers',
            required=False
        )

    class Meta(GroupBaseForm.Meta):
        exclude = ['headman', 'teachers']
