from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import StudentCreateForm
from .models import Students
from .forms import StudentsFilter


class StudentsListView(ListView):
    paginate_by = 10
    model = Students
    template_name = 'students/list.html'

    def get_filter(self):
        return StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_forms'] = self.get_filter().form

        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Student {} successfully has been created'.format(
            self.object))

        return result


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(self.request, 'Student {} successfully has been changed'.format(self.object))

        return result


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Students
    template_name = 'students/students_confirm_delete.html'
    success_url = reverse_lazy('students:list')

    def delete(self, request, *args, **kwargs):
        res = super(StudentDeleteView, self).delete(request, *args, **kwargs)
        messages.success(self.request, 'Student {} successfully removed'.format(
            self.object))
        return res

