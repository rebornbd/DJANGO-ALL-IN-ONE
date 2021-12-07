from django.db import models

class Book(models.Model):
  title   = models.CharField(max_length=200)
  writer  = models.CharField(max_length=200)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
