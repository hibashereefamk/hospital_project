from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dep_name=models.ForeignKey(Department,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')
    def __str__(self):
        return self.doc_name + '-('+self.doc_spec +')'
class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone = models.CharField(max_length=10)
    p_email =models.EmailField()
    doc_name = models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date= models.DateField()
    booked_on =models.DateField(auto_now =True)

    def __str__(self):
        
        return f"{self.p_name} - {self.doc_name.doc_name} on {self.booking_date}"
    
class Contacts(models.Model):
    p_name = models.CharField(max_length=100)
    p_email= models.EmailField()
    doc_name =models.ForeignKey(Doctors,on_delete=models.CASCADE, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    message=models.TextField()
class Feedback(models.Model):
    P_name =models.CharField(max_length=100)
    p_email =models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),
        MaxValueValidator(5)]
    )
    message=models.TextField()
    

