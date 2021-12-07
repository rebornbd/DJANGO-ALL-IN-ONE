from django.http import HttpResponse
from django.shortcuts import render
from .tasks import add, mul


def home(request):
  # celery task assign

  # delay
  add.delay(10, 10)

  # apply_async
  # add.apply_async((10, 10))
  # add.apply_async(args=(10, 10))
  # add.apply_async(args=(10, 10), kwargs=None)
  # add.apply_async(args=(10, 10), kwargs={})
  
  # task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
  # task.s(arg1, arg2, kwarg1='x', kwargs2='y').apply_async()

  # get user response as possible
  return HttpResponse("done!")
