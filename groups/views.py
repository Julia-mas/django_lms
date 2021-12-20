from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Groups
from groups.forms import GroupsFilter

from webargs import fields
from webargs.djangoparser import use_args


@use_args(
    {
        'groups_name': fields.Str(required=False),
        'groups_nationality': fields.Str(required=False),
        'groups_language': fields.Str(required=False),
        'members_qty': fields.Str(required=False)
     },
    location='query'
)
def get_groups(request, args):
    groups = Groups.objects.all()

    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})

    filter_groups = GroupsFilter(data=request.GET, queryset=groups)

    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups, 'filter_groups': filter_groups}
    )


def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


def update_group(request, pk):
    group = Groups.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_group(request, pk):
    group = get_object_or_404(Groups, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
