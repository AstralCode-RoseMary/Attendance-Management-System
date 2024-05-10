from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Example view function
def index(request):
    return HttpResponse("Hello, world. You're at the index page.")
