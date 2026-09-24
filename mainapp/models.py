from django.db import models

# Create your models here.
class Admin(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)   
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    session = models.CharField(max_length=50)
    address = models.TextField()
    pic = models.FileField(max_length=255, upload_to="student", null=True, blank=True)
    regdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Login(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.name} ({self.email})"


    

    

