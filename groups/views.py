from django.http import HttpResponse
from django.shortcuts import render


def index_group(request):
    return HttpResponse('<h1>Hello my dear friend!</h1>')
