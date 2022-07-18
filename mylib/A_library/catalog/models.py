from textwrap import fill
from django.db import models
from ast import Delete
from distutils.command.upload import upload
from turtle import title
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User
import uuid # Required for unique book instances
# Create your models here.
from django.db import models
from .validators import(validate_firstname_length,
 validate_lastname_length,
 validate_username_length, validate_username_alphadigits,
 validate_password_length, validate_password_digit,
 validate_password_uppercase, 
 validate_phonenumber)



class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    title = models.TextField(max_length=120)
    isbn = models.CharField('ISBN', max_length=13, null=True,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.TextField(max_length=120,  help_text='Enter field documentation')
    description = models.TextField(blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    subject_area = models.TextField(blank=False, null=False)
    uploaded_by = models.TextField(max_length=120,null=True,blank=True)
    book_status = (
        ('b', 'borrowed'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=120,choices=book_status,blank=True,default='b',help_text='Book availability',)
    pdf = models.FileField(upload_to='A_library/pdfs/',null=True,blank=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True   
class Meta:
        Borrower = ['due_back'] 

        def __str__(self):
            """String for representing the Model object."""
            return str(self.isbin)+"["+str(self.isbn)+']'  

def get_expiry():
    return datetime.today() + timedelta(days=7)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=True)
    student_id = models.TextField(primary_key=True,max_length=120,null=False,blank=True)
    student_name = models.TextField(blank=True, null=True)
    registration_no = models.TextField(max_length=120)
    phone = models.CharField(max_length=10, blank=True)
    gender = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    gender = models.CharField(max_length=1,choices= gender,blank=True,default='b')
    email= models.EmailField(max_length=120,default=True, null=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True 

    def __str__ (self):
        """String for representing the Model object."""
        return '{}'.format(self.registration_no) 
## there was a repitition of borrwer and payment yet  can taken as one

class Borrower(models.Model):
    student_id = models.TextField(primary_key=True, max_length=120,null=False,default=True)
    book_id = models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    fine_amount= models.TextField(default=True, null=False)
    date_borrowed= models.DateField(max_length=120,auto_now=True)
    date_returned=models.DateField(max_length=120)
    expected_date_return = models.DateField(max_length=120,auto_now=True)
    Featured = models.BooleanField(default=True,null=True) # null=True, default=True 
    
    def __str__(self):
        """String for representing the Model object."""
        return '{}'.format(self.date_borrowed) 


class Siteuser(models.Model):
    firstname= models.CharField(max_length=100, verbose_name='First name', validators= [validate_firstname_length])
    lastname= models.CharField(max_length=100, verbose_name='Last name', validators= [validate_lastname_length])
    username= models.CharField(max_length=25, verbose_name= 'User name', validators= [validate_username_length, validate_username_alphadigits])
    password1= models.CharField(max_length=30, validators=[validate_password_length, validate_password_digit, validate_password_uppercase])
    password2= models.CharField(max_length=30)
    birth_date= models.DateField(verbose_name='What is your birth date?')
    gender= models.CharField(max_length=6)
    email= models.EmailField()
    phone= models.CharField(max_length= 15, validators= [validate_phonenumber])
    location= models.CharField(max_length=100)    

## some logic

def get_expiry():
    return datetime.today() + timedelta(days=15)

def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])     
