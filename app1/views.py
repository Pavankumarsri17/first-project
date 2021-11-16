from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return HttpResponse("<h1><marquee>King of Cricket</marquee></h>")