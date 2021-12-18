from django.http import HttpResponseRedirect
from django.shortcuts import render # noqa
from django.views.decorators.csrf import csrf_exempt

from groups.forms import GroupCreateForm
from groups.models import Groups
# from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


def index_group(request):
    return render(request, 'groups/index.html')


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

    return render(
        request=request,
        template_name='groups/list.html',
        context={'groups': groups}
    )


def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(
        request=request,
        template_name='groups/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_group(request, pk):
    group = Groups.objects.get(id=pk)
    if request.method == 'GET':
        form = GroupCreateForm(instance=group)
    elif request.method == 'POST':
        form = GroupCreateForm(data=request.POST, instance=group)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups/')

    return render(request, 'groups/update.html', {'form': form})
