from django.http import HttpResponse
from django.shortcuts import render  # noqa

from webargs.djangoparser import use_kwargs, use_args
from webargs import fields, validate

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

    html_form = """
        <form method="get">
            <label for="fname">First name:</label>
            <input type="text" id="fname" name="first_name"></br></br>

            <label for="lname">Last name:</label>
            <input type="text" id="lname" name="last_name"></br></br>

            <label for="age">Age:</label>
            <input type="number" name="age"></br></br>

            <input type="submit" value="Submit">
        </form>
    """

    records = format_records(students)

    response = html_form + records

    return HttpResponse(response)




