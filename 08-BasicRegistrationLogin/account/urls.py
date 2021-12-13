from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from . import views


urlpatterns = [
  path('signin', TokenObtainPairView.as_view(), name='user_signinToken'),
  path('signin/refresh-token', TokenRefreshView.as_view(), name='user_refreshToken'),
  path('signup', views.RegisterUserView.as_view(), name='user_signup'),
]
