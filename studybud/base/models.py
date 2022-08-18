
from django.db import models
import uuid # Required for unique book instances
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
  
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    business_book=models.BooleanField(default=False)
    science_books=models.BooleanField(default=False)
    
    
    def __str__(self):
      return self.name


'''class BorrowRecord(models.Model):
  student_id = models.TextField(primary_key=True, max_length=120,null=False,default=True)
  book=models.CharField(max_length=200)
  fine_amount= models.TextField(default=True, null=False)
  borrow_date= models.DateField(max_length=120,auto_now=True)
  return_date=models.DateField(max_length=120,auto_now=True)
  expected_date_return = models.DateField(max_length=120,auto_now=True)
  Featured = models.BooleanField(default=True,null=True) # null=True, default=True 
  #def __str__(self):
        """String for representing the Model object."""
        return '{}'.format(self.date_borrowed) '''


class BookInstance(models.Model):
      id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
      book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
      due_back = models.DateField(null=True, blank=True)
      borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
     

      book_status = (
        ('b', 'borrowed'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
      status = models.CharField(max_length=120,choices=book_status,blank=True,default='b',help_text='Book availability',)
      Featured = models.BooleanField(default=True,null=True) # null=True, default=True   
    
class status(models.Model):
      book_status = (
        ('b', 'borrowed'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
      status = models.CharField(max_length=120,choices=book_status,blank=True,default='b',help_text='Book availability',)
   




##request book
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    date_requested = models.DateField(auto_now_add=True)
    return_date=models.DateTimeField(null=True)
    status = models.ForeignKey(Book, on_delete=models.CASCADE, null=True,related_name="+")

    def __str__(self):
        return  self.book