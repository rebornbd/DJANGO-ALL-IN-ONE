from django.http.response import StreamingHttpResponse
from django.views.generic import View
from django.http import JsonResponse
import json

from ..models import Book
from .fbv import BookSerializer


# method implementations
class CBV_View(View):
  def get(self, request):
    books = Book.objects.all()
    data = BookSerializer(books)
    return JsonResponse(data, safe=False)

  
  def post(self, request, *args, **kwargs):
    res = {}
    try:
      body = json.loads(request.body)
      title = body.get('title', '')
      writer = body.get('writer', '')

      if title == None or title == "":
        raise ValueError('title is empty')
      
      if writer == None or writer == "":
        raise ValueError('writer is empty')

      book = Book.objects.create(title=title, writer=writer)
      res = {
        "title": book.title,
        "writer": book.writer
      }
    except Exception as err:
      res = {
        "success": False,
        "message": str(err)
      }
    return JsonResponse(res)


  def put(self, request, *args, **kwargs):
    res = {}
    try:
      body = json.loads(request.body)
      id = body.get('id')
      title = body.get('title', '')
      writer = body.get('writer', '')

      book = Book.objects.get(pk=id)

      if title == None or title == "":
        raise ValueError('title is empty')
      
      if writer == None or writer == "":
        raise ValueError('writer is empty')

      book.title = title
      book.writer = writer
      book.save()

      res = {
        "title": book.title,
        "writer": book.writer
      }

    except Exception as err:
      res = {
        "success": False,
        "message": str(err)
      }
    return JsonResponse(res)

  
  def delete(self, request, *args, **kwargs):
    res = {}
    try:
      body = json.loads(request.body)
      id = body.get('id')

      book = Book.objects.get(pk=id)
      book.delete()

      res = {
        "id": id,
        "title": book.title,
        "writer": book.writer
      }
    except Exception as err:
      res = {
        "success": False,
        "message": str(err)
      }
    return JsonResponse(res)
