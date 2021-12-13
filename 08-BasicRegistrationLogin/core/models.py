from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=100)
  desc = models.TextField(null=True, blank=True)

  def __str__(self):
    return self.name


class Book(models.Model):
  title = models.CharField(max_length=100)
  writers = models.ManyToManyField(to=Author, related_name='books')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
