from django import forms
from .models import Booking


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
            "booking_date":"Bookibng date:",
            

        }

