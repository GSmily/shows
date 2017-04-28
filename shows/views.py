from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponsse('hey')

def detail(request, show_id):
    return HttpResponse("You're looking at show %s." % show_id)

def rating(request, show_id):
    response = "You're looking at the rating of show %s."
    return HttpResponse(response % show_id)

def rate(request, show_id):
    return HttpResponse("You're rating on show %s." % show_id)