from django.contrib import admin
from django.contrib import admin
from.models import Book,Student,Borrower
from.models import Student
from.models import Borrower

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Borrower)

