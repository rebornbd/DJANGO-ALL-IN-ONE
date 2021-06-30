from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (FBV_ListView, FBV_CreateView, FBV_UpdateView, 
                    FBV_DeleteView, CBV_View)


urlpatterns = [
    path('', FBV_ListView),
    path('create', csrf_exempt(FBV_CreateView)),
    path('update', csrf_exempt(FBV_UpdateView)),
    path('remove', csrf_exempt(FBV_DeleteView)),

    path('cbv', csrf_exempt(CBV_View.as_view())),
]
