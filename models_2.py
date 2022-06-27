from ast import Delete
from distutils.command.upload import upload
from turtle import title
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_Librarian=models.BooleanField(default=False)
    class Meta:
        swappable='AUTH_USER_MODEL'

class Book(models.Model):
    book_id = models.TextField(max_length=120)
    title = models.TextField(max_length=120)
    author = models.TextField(max_length=120)
    description = models.TextField(blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    subject_area = models.TextField(blank=False, null=False)
    uploaded_by = models.TextField(max_length=120,null=True,blank=True)
    pdf = models.FileField(upload_to='A_library/pdfs/',null=True,blank=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True   
             
class Students(models.Model):
    student_id = models.TextField(max_length=120,null=True,blank=True)
    student_name = models.TextField(blank=True, null=True)
    registration_no = models.TextField(max_length=120)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True 

class Payments(models.Model):
    payment_id = models.TextField(max_length=120)
    fine_ammount= models.TextField(max_length=120)
    payment = models.TextField(blank=True, null=True)
    book_id = models.TextField(blank=False, null=False)
    student_id = models.TextField(max_length=120,null=True,blank=True)
    uploaded_by = models.TextField(max_length=120,null=True,blank=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True 

class Borrowers(models.Model):
    student_id = models.TextField(max_length=120,null=True,blank=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True 
    date_borrowed= models.DateField(max_length=120)
    date_returned=models.DateField(max_length=120)
    book_id = models.TextField(blank=False, null=False)
    expected_date_return = models.DateField(max_length=120)
    