from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from groups.forms import GroupCreateForm, GroupUpdateForm
from groups.models import Groups
from groups.forms import GroupsFilter

from webargs import fields
from webargs.djangoparser import use_args

from students.models import Students


@use_args(
    {
        'groups_name': fields.Str(required=False),
        'groups_country': fields.Str(required=False),
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


def delete_group(request, pk):
    group = get_object_or_404(Groups, id=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})


class GroupListView(ListView):
    model = Groups
    template_name = 'groups/list.html'


class GroupCreateView(CreateView):
    model = Groups
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(UpdateView):
    model = Groups
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_fields'] = self.object.headman.id
        except AttributeError as ex:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = form.cleaned_data['headman_field']
        if pk:
            form.instance.headman = Students.objects.get(id=form.cleaned_data['headman_field'])
        form.instance.save()

        return response


class GroupDeleteView(DeleteView):
    model = Groups
    success_url = reverse_lazy('groups:list')
