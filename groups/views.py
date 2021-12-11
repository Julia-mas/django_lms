from django.http import HttpResponse
from django.shortcuts import render # noqa

from groups.models import Groups
from groups.utils import format_records

from webargs import fields
from webargs.djangoparser import use_args


def index_group(request):
    return HttpResponse('<h1>Hello my dear friend!</h1>')


@use_args(
    {
        'groups_name': fields.Str(required=False),
        'groups_nationality': fields.Str(required=False),
        'groups_language': fields.Str(required=False),
        'members_qty': fields.Str(required=False)
     },
    location='query'
)
def get_groups(request, args):
    groups = Groups.objects.all()

    for key, value in args.items():
        if value:
            groups = groups.filter(**{key: value})

    html_form = """
        <form method="get">
            <label for="gname">Groups name:</label>
            <input type="text" id="gname" name="groups_name"></br></br>
            <label for="gnat">Groups nationality:</label>
            <input type="text" id="gnat" name="groups_nationality"></br></br>
            <label for="language">Groups language:</label>
            <input type="text" name="groups_language"></br></br>
            <label for="members">Members quantity:</label>
            <input type="number" name="members_qty"></br></br>
            <input type="submit" value="Submit">
        </form>
    """

    records = format_records(groups)
    response = html_form + records
    return HttpResponse(response)
