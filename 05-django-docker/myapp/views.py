from django.http import HttpResponse


def Hello(request):
  return HttpResponse("Welcome first docker demo-project!")
