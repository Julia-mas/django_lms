from django.http import HttpResponse
from django.shortcuts import render


def index_teachers(request):
    return HttpResponse('<h1>Teachers views!</h1>')
