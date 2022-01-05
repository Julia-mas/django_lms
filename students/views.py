
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView, DeleteView

from .forms import StudentCreateForm
from .models import Students
from .forms import StudentsFilter


class StudentsListView(ListView):
    model = Students
    template_name = 'students/list.html'

    def get_queryset(self):
        filter_students = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

        return filter_students


class StudentCreateView(CreateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('student:list')
