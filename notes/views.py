from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_notes(request):
    output = ''
    output += "<html><head><title>"
    output += "First Python Heroku Deployment"
    output += "</title></head>"
    output += "<body>"
    output += "<h1>Sprint Challenge - Python Django Heroku</h1>"
    output += "<p>My First Python Heroku Deployment.</p>"
    output += "</body></html>"
    return HttpResponse(output)

