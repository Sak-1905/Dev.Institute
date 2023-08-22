from django.http import HttpResponse 
from django.shortcuts import render
from django.template import loader

from .models import Driver


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def status(request):
    return HttpResponse("Website is up and running")

def about(request):
    username="John"
    ctx = {  #context contains all the variables and objects that you want to render the template with 
        'username': username
    }
    template = loader.get_template('polls/about.html')
    return HttpResponse(template.render(ctx, request))


def drivers(request):

    ctx={
        'name': 'Nirmal',
        'drivers': Driver.objects.all().order_by('id')
    }
    
    
    template = loader.get_template('polls/drivers.html')
    return HttpResponse(template.render(ctx, request))

def test(request):
    if request['method']=='GET':
        return HttpResponse("This is a test page")
    
    # else:
    #     return HttpResponse("This is a test page")