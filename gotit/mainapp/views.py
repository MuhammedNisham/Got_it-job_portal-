from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse

from .models import Job


# Create your views here.

def homeView(request):
    template = loader.get_template('home.html')

    context = {
        'jobs' : Job.objects.all()
    }
    return HttpResponse(template.render(context, request))

def jobView(request):
    template = loader.get_template('jobs.html')

    context = {}
    return HttpResponse(template.render(context, request))
