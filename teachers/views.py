from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from teachers.forms import TeacherCreateForm, TeacherUpdateForm
from teachers.models import Teachers
from teachers.forms import TeachersFilter


class TeacherListView(ListView):
    model = Teachers
    template_name = 'teachers/list.html'

    def get_queryset(self):
        filter_teachers = TeachersFilter(
            data=self.request.GET,
            queryset=self.model.objects.all()
        )
        return filter_teachers


class TeacherCreateView(CreateView):
    model = Teachers
    form_class = TeacherCreateForm
    success_url = reverse_lazy('teacher:list')
    template_name = 'teachers/create.html'


class TeacherUpdateView(UpdateView):
    model = Teachers
    form_class = TeacherUpdateForm
    success_url = reverse_lazy('teacher:list')
    template_name = 'teachers/update.html'


class TeacherDeleteView(DeleteView):
    model = Teachers
    success_url = reverse_lazy('teachers:list')





