from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from groups.forms import GroupCreateForm, GroupUpdateForm, GroupsFilter
from groups.models import Groups

from students.models import Students


class GroupListView(ListView):
    model = Groups
    template_name = 'groups/list.html'

    def get_queryset(self):
        filter_groups = GroupsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().prefetch_related('students')
        )
        return filter_groups


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Groups
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'


class GroupUpdateView(LoginRequiredMixin, UpdateView):
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


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Groups
    success_url = reverse_lazy('groups:list')
