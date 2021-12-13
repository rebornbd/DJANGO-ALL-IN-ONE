from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
  permission_classes = (IsAuthenticated, )

  def get(self, request, *args, **kwargs):
    res = dir(request)
    user = request.user

    print(res)
    content = {'message': 'Hello, World!'}
    return Response(content)
