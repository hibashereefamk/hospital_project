from django.contrib import admin
from.models import Department,Doctors,Booking,Register,Login

admin.site.register(Department)
admin.site.register(Doctors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date',"booked_on")



admin.site.register(Booking,BookingAdmin)
admin.site.register(Register)
admin.site.register(Login)