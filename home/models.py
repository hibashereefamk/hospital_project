from django.db import models


class Department(models.Model): 
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()


