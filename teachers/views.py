from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm
from teachers.models import Teachers


from webargs import fields
from webargs.djangoparser import use_args


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'subject': fields.Str(required=False),
        'seniority_years': fields.Int(required=False),
        'phone_number': fields.Int(required=False)
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teachers.objects.all()
    for key, value in args.items():
        if value:
            teachers = teachers.filter(**{key: value})

    return render(
        request=request,
        template_name='teachers/list.html',
        context={'test': 'Hello World!', 'teachers': teachers}
    )


def create_teacher(request):
    if request.method == "GET":
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(
        request=request,
        template_name='teachers/create.html',
        context={'form': form}
    )


@csrf_exempt
def update_teacher(request, pk):
    teacher = Teachers.objects.get(id=pk)
    if request.method == 'GET':
        form = TeacherCreateForm(instance=teacher)
    elif request.method == 'POST':
        form = TeacherCreateForm(data=request.POST, instance=teacher)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    # html_form = f"""
    #     <form method="post">
    #         {form.as_p()}
    #
    #         <input type="submit" value="Update">
    #     </form>
    # """
    return render(request, 'teachers/update.html', {'form': form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, id=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})


