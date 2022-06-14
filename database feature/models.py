from turtle import title
from django.db import models
# Create your models here.
class book(models.Model):
    title = models.TextField(max_length=120)
    author = models.TextField(max_length=120)
    description = models.TextField(blank=True, null=True)
    date_of_publication = models.TextField(blank=True, null=True)
    subject_area = models.TextField(blank=False, null=False)
    Featured = models.BooleanField() # null=True, default=True