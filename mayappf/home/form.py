from django import forms
from .models import Booking,Contacts,Feedback


class DateInput(forms.DateInput):
    input_type ='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = '__all__'
    

        widgets={
            'booking_date': DateInput(),
            'doc_name': forms.Select(attrs={'style': 'width: 250px;'}),
        }
        labels ={
            'p_name':"Patient Name:",
            'p_phone':"Patient phone:",
            'p_email':"Patient Email:",
            'doc_name':"Doctors Name:",
            "booking_date":"Booking date:",
            

        }
class contactform(forms.ModelForm):
    class Meta:
        model=Contacts
        fields='__all__'
        
        labels={
            'p_name':'Enter Name :',
            'p_email':"Enter Name :",
            'doc_name':"Doctor :",
            'phone':'phone :',
            'message':"Message :"
        }
        widgets ={
            'p_name':forms.TextInput(attrs={'placeholder': 'your name','class': 'form_control'}),
            'p_email':forms.EmailInput(attrs={'placeholder': ' example.gmail.com','class': 'form_control'}),
            'doc_name':forms.Select(attrs={'class': 'form_control','style': 'width: 250px;'}),
            'phone':forms.NumberInput(attrs={'placeholder': 'phone number','class': 'form_control'}),
            'message':forms.Textarea(attrs={'placeholder': ' write your message here','class': 'form_control','rows':4})
            }

class feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        labels={
            'P_name':'Enter Name :',
            'p_email':"Enter Email :",
            'doc_name':"doctor :",
            'rating':'Rating (1-5) :',
            'message':"Message :"
        }
        widgets={
            'P_name':forms.TextInput(attrs={'placeholder': 'your name','class': 'form_control'}),
            'p_email':forms.EmailInput(attrs={'placeholder': ' example.gmail.com','class': 'form_control'}),
            'doc_name':forms.Select(attrs={'class': 'form_control','style': 'width: 250px'}),
            'rating':forms.NumberInput(attrs={'placeholder': '1-5','class': 'form_control'}),
            'message':forms.Textarea(attrs={'placeholder': ' write your message here','class': 'form_control','rows':4})
            }
