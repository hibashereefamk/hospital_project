from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Department,Doctors,Booking
from .form import BookingForm


def index(request):
    
    return render(request,'index.html')
def register(request):
    
    return render(request,'register.html')
def login(request):
    
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    
    form = BookingForm()
    dict_form={
   'form': form
    }
    

    
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docts={
        "doctors":Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docts)

def contacts(request):
    return render(request,'contacts.html')

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)


