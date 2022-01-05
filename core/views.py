from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from students.forms import StudentCreateForm
from students.models import Students


def index(request):
    return render(request, 'index.html')


class UpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    @classmethod
    def update_class(cls, request, pk):
        obj = get_object_or_404(cls.model, id=pk)

        if request.method == 'GET':
            form = cls.form_class(instance=obj)
        elif request.method == 'POST':
            form = cls.form_class(data=request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(cls.success_url))

        return render(
            request,
            cls.template_name,
            {'form': form}
        )


