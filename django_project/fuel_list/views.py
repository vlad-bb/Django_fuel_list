from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    text = 'Hello'
    return render(request, 'fuel_list/index.html', {"text": text})
