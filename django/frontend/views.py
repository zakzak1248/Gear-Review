from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def index(request):
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    return render(request, "templates/index.html")