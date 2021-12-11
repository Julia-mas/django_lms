from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render  # noqa
from django.views.decorators.csrf import csrf_exempt

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields, validate

from .forms import StudentCreateForm
from .models import Students
from .utils import format_records


def index(request):
    return HttpResponse('<h1>Hello from Django!</h1>')


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'age': fields.Int(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Students.objects.all()

    for key, value in args.items():
        if value:
            students = students.filter(**{key: value})

    # html_form = """
    #     <form method="get">
    #         <label for="fname">First name:</label>
    #         <input type="text" id="fname" name="first_name"></br></br>
    #
    #         <label for="lname">Last name:</label>
    #         <input type="text" id="lname" name="last_name"></br></br>
    #
    #         <label for="age">Age:</label>
    #         <input type="number" name="age"></br></br>
    #
    #         <input type="submit" value="Submit">
    #     </form>
    # # """
    #
    # records = format_records(students)
    #
    # response = html_form + records

    # return HttpResponse(response)
    return render(request=request,
                  template_name='students/list.html',
                  context={'test': 'Hello World!'}

    )


@csrf_exempt
def create_student(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    html_form = f"""
        <form method="post">
            {form.as_p()}

            <input type="submit" value="Submit">
        </form>
    """

    return HttpResponse(html_form)


# @csrf_exempt
def update_student(request, pk):
    student = Students.objects.get(id=pk)
    if request.method == 'GET':
        form = StudentCreateForm(instance=student)
    elif request.method == 'POST':
        form = StudentCreateForm(data=request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    # html_form = f"""
    #     <form method="post">
    #         {form.as_p()}
    #
    #         <input type="Search" value="Submit">
    #     </form>
    # """
    #
    # return HttpResponse(html_form)
    return render(
        request=request,
        template_name='students'

    )