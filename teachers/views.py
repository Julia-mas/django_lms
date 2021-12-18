from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse # noqa
from django.views.decorators.csrf import csrf_exempt

from teachers.forms import TeacherCreateForm
from teachers.models import Teachers
# from teachers.utils import format_records


from webargs import fields
from webargs.djangoparser import use_args


def index_teachers(request):
    return render(request, 'teachers/index.html')


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
            return HttpResponseRedirect('/teachers/')

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
            return HttpResponseRedirect('/teachers/')

    # html_form = f"""
    #     <form method="post">
    #         {form.as_p()}
    #
    #         <input type="submit" value="Update">
    #     </form>
    # """
    return render(request, 'teachers/update.html', {'form': form})


