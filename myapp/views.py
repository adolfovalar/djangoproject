from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("About")

