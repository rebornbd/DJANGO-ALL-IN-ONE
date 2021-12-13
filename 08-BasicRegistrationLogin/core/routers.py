from rest_framework import routers
from .viewsets import AuthorViewset, BookViewset


authorRouter = routers.SimpleRouter()
authorRouter.register(r'', AuthorViewset)

bookRouter = routers.SimpleRouter()
bookRouter.register(r'', BookViewset)
