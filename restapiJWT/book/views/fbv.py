from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from dotenv import dotenv_values
import datetime
import json
import jwt

from ..serializer import BookSerializer
from ..models import Book


MYCONFIG  = dotenv_values(".env")
SECRETKEY = MYCONFIG["MYSECRET_KEY"]

def LoginView(request):
    data = {}
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            username = body.get('username', '')
            password = body.get('password', '')

            user = User.objects.filter(username=username).first()

            generalUser(user)
            passwordMatched(user, password)

            response = setJWT(user.id)
            return response
        except Exception as err:
            data = {
                "success": False,
                "message": str(err)
            }
    return JsonResponse(data)


def LogoutView(request):
    if request.method == 'POST':
        response = removeJWT()
        return response
    
    data = {
        "success": False
    }
    return JsonResponse(data)


def FBV_ListView(request):
    data = {}
    if request.method == "GET":
        try:
            books = Book.objects.all()
            data = BookSerializer(books)
            return JsonResponse(data, safe=False)
        except Exception as err:
            data = {
                "success": False,
                "message": str(err)
            }
    return JsonResponse(data)


def FBV_CreateView(request):
    data = {}
    if request.method == "POST":
        try:
            body   = json.loads(request.body)
            title  = body.get('title', '')
            writer = body.get('writer', '')

            token = getToken(request)
            user  = tokenToUser(token)

            generalUser(user)
            # adminUser(user)

            bookValidity(title, writer)

            book = Book(title=title, writer=writer)
            book.save()

            data = {
                "title": book.title,
                "writer": book.writer
            }
            return JsonResponse(data)
        except Exception as err:
            data = {
                "success": False,
                "message": str(err)
            }
    return JsonResponse(data)


def FBV_UpdateView(request):
    data = {}
    if request.method == "PUT":
        try:
            body    = json.loads(request.body)
            id      = body.get('id')
            title   = body.get('title', '')
            writer  = body.get('writer', '')

            token = getToken(request)
            user  = tokenToUser(token)

            generalUser(user)
            # adminUser(user)

            book = Book.objects.get(pk=id)
            bookValidity(title, writer)

            book.title  = title
            book.writer = writer
            book.save()

            data = {
                "title": book.title,
                "writer": book.writer
            }
            return JsonResponse(data)
        except Exception as err:
            data = {
                "success": False,
                "message": str(err)
            }
    return JsonResponse(data)


def FBV_DeleteView(request):
    data = {}
    if request.method == "DELETE":
        try:
            body    = json.loads(request.body)
            id      = body.get('id')

            token = getToken(request)
            user  = tokenToUser(token)

            generalUser(user)
            adminUser(user)

            book = Book.objects.get(pk=id)
            book.delete()
            
            data = {
                "removed": True,
                "title": book.title,
                "writer": book.writer
            }
            return JsonResponse(data)
        except Exception as err:
            data = {
                "success": False,
                "message": str(err)
            }
    return JsonResponse(data)



# ========== dependency methods ================
def generalUser(user):
    if user is None:
        raise ValueError('User Not Found!')
    
    if not user.is_active:
        raise ValueError('User Not Active!')


def adminUser(user):
    if not user.is_superuser:
        raise ValueError('User Not Admin!')


def passwordMatched(user, password):
    if not user.check_password(password):
        raise ValueError('Incorrect Password!')


def setJWT(userID):
    try:
        response = HttpResponse()

        payload = {
            'id': userID,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, SECRETKEY, algorithm='HS256')

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    except Exception as err:
        raise ValueError(str(err))


def removeJWT():
    response = HttpResponse()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


def getToken(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise ValueError('Unauthenticated User!')
    return token


def tokenToUser(token):
    user = None
    try:
        payload = jwt.decode(token, SECRETKEY, algorithms=['HS256'])

        userId = payload['id']
        user = User.objects.filter(id=userId).first()
    except Exception as err:
        raise ValueError(str(err))
    return user


def bookValidity(title="", writer=""):
    if title is None or title == "":
        raise ValueError('Book Title Is Empty!')

    if writer is None or writer == "":
        raise ValueError('Book Writer Is Empty!')
