from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>this is my first view in app1</h1>')
def second(request):
    return HttpResponse('<marquee><h1>this is my second view in app2</h1></marquee>')
def third(request):
    return HttpResponse('<marquee><h1>welcome to my world </h1></marquee>')
