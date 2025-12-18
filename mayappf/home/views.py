from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Doctors
from .form import BookingForm,contactform,feedbackform
from django.contrib.auth.decorators import login_required


def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

@login_required
def booking(request):
    if request.method == 'POST':
        form= BookingForm(request.POST)
        if form.is_valid():
            booking=form.save()
            return render(request,'confirmation.html',{'booking':booking})
    
    form = BookingForm()
    return render(request,'booking.html',{'form': form})

def doctors(request):
    dict_docts={
        "doctors":Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docts)

@login_required
def contacts(request):
    if request.method =='POST':
        form =contactform(request.POST)
        if form.is_valid():
            contact=form.save()
            return render(request,'confirmation.html', {'contact': contact})
    form= contactform()
    return render(request,'contacts.html',{'form':form})

@login_required
def feedback(request):
    if request.method =='POST':
        form =feedbackform(request.POST)
        if form.is_valid():
            feedback=form.save()
            return render(request,'confirmation.html', {'feedback': feedback})
        
    form=feedbackform()
    return render(request,'feedback.html',{"form":form})


    

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)