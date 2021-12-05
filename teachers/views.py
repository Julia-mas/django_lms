from django.http import HttpResponse
from django.shortcuts import render # noqa

from teachers.models import Teachers
from teachers.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


def index_teachers(request):
    return HttpResponse('<h1>Teachers views!</h1>')


@use_args(
    {
        'first_name': fields.Str(required=False),
        'last_name': fields.Str(required=False),
        'subject': fields.Str(required=False),
        'seniority_years': fields.Int(required=False),
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teachers.objects.all()
    for key, value in args.items():
        if value:
            teachers = teachers.filter(**{key: value})
    html_form = """
        <form method="get">
            <label for="fname">First name:</label>
            <input type="text" id="fname" name="first_name"></br></br>
            <label for="lname">Last name:</label>
            <input type="text" id="lname" name="last_name"></br></br>
            <label for="subject">Subject:</label>
            <input type="text" name="subject"></br></br>
            <label for="years">Seniority years:</label>
            <input type="number" name="seniority_years"></br></br>
            <input type="submit" value="Submit">
        </form>
    """
    records = format_records(teachers)
    response = html_form + records
    return HttpResponse(response)
