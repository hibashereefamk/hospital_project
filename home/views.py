from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1> home world </h1>')
def about(request):
    return HttpResponse('about page')
def booking(request):
    return HttpResponse('booking page')
def doctors(request):
    return HttpResponse('doctors page')
def contacts(request):
    return HttpResponse('contacts page')

