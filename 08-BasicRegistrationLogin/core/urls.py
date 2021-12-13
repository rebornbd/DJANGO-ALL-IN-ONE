from django.urls import path, include
from . import views
from . import routers


urlpatterns = [
  path('author/', include(routers.authorRouter.urls)),
  path('book/', include(routers.bookRouter.urls)),
]
