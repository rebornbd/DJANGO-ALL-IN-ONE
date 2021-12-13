from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
  path('get-token-cbv', obtain_auth_token, name='api_get_token_cbv'),
  path('get-token-fbv', views.login, name='api_get_token_fbv'),
]
