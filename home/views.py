from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    person={
        'name':"john",
        'age':22,
        "place":"karaparamba"

    }
    numbers=[2,3,4,5,6,6]
    return render(request,'index.html', {'person': person, 'numbers': numbers})
def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')
def doctors(request):
    return render(request,'doctors.html')
def contacts(request):
    return render(request,'contacts.html')
def department(request):
    return render(request,'department.html')

