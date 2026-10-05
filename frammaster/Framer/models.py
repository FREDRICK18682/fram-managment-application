from django.db import models

# Create your models here
class UserProfile(models.Model):
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Phone_number = models.CharField(max_length=10)
    Gender = models.CharField(max_length=6)
    Id_number = models.CharField(max_length=10)
    Date_Birth = models.DateField()

    def __str__(self):
        return self.name