from django.http import JsonResponse
import json

from ..models import Book


def BookSerializer(books):
  res = []
  for indx in range(0, len(books)):
    book = books[indx]

    data = {
      "id": book.id,
      "title": book.title,
      "writer": book.writer
    }
    res.append(data)
  return res

# method implementations
def FBV_ListView(request):
  books = Book.objects.all()
  data = BookSerializer(books)
  return JsonResponse(data, safe=False)



def FBV_CreateView(request):
  data = {
    "success": False,
    "message": "method is not valid!"
  }
  if request.method == 'POST':
    try:
      body = json.loads(request.body)
      title = body.get('title', '')
      writer = body.get('writer', '')

      if title == None or title == "":
        raise ValueError('title is empty')
      
      if writer == None or writer == "":
        raise ValueError('writer is empty')

      book = Book.objects.create(title=title, writer=writer)
      data = {
        "title": book.title,
        "writer": book.writer
      }
    except Exception as err:
      data = {
        "success": False,
        "message": str(err)
      }
  return JsonResponse(data)



def FBV_UpdateView(request):
  data = {
    "success": False,
    "message": "method is not valid!"
  }
  if request.method == 'PUT':
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

      data = {
        "title": book.title,
        "writer": book.writer
      }

    except Exception as err:
      data = {
        "success": False,
        "message": str(err)
      }
  return JsonResponse(data)



def FBV_DeleteView(request):
  data = {}
  if request.method == 'DELETE':
    try:
      body = json.loads(request.body)
      id = body.get('id')

      book = Book.objects.get(pk=id)
      book.delete()

      data = {
        "id": id,
        "title": book.title,
        "writer": book.writer
      }
    except Exception as err:
      data = {
        "success": False,
        "message": str(err)
      }
  return JsonResponse(data)
