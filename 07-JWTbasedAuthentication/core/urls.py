from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from . import views


urlpatterns = [
  path('token', TokenObtainPairView.as_view(), name='token'),
  path('refresh-token', TokenRefreshView.as_view(), name='refresh_token'),

  path('hello', views.HelloView.as_view(), name='hello'),
]
