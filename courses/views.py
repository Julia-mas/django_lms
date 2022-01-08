from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from courses.forms import CourseCreateForm, CoursesFilter
from courses.models import Course


def get_course(request):
    courses = Course.objects.all().select_related('group')
    filter_courses = CoursesFilter(data=request.GET, queryset=courses)

    return render(
        request,
        'courses/list.html',
        {'filter_courses': filter_courses})


def create_course(request):
    if request.method == 'GET':
        form = CourseCreateForm()

    elif request.method == 'POST':
        form = CourseCreateForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/create.html', {'form': form})


@login_required
def update_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'GET':
        form = CourseCreateForm(instance=course)

    elif request.method == 'POST':
        form = CourseCreateForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('courses:get'))

    return render(request, 'courses/update.html', {'form': form})


@login_required
def delete_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('courses:list'))

    return render(request, 'courses/students_confirm_delete.html', {'course': course})

