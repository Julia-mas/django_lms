from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView

from webargs.djangoparser import use_args
from webargs import fields


from .forms import StudentCreateForm
from .models import Students
from .forms import StudentsFilter


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False),
    },
    location='query'
)
def get_students(request):
    students = Students.objects.all().select_related('group', 'headman_group')
    filter_students = StudentsFilter(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={'test': 'Hello World!',
                 'students': students,
                 'filter_students': filter_students
                 }
    )


def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={'form': form}
    )


def delete_student(request, pk):
    student = get_object_or_404(Students, id=pk)
    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})


class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentCreateForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/update.html'


class StudentsListView(ListView):
    model = Students
    template_name = 'students/list.html'

    def get_queryset(self):
        filter_students = StudentsFilter(
            data=self.request.GET,
            queryset=self.model.objects.all().select_related('group', 'headman_group')
        )

        return filter_students
