from django.urls import path

from . views import index1 

urlpatterns = [
    path('user/', index1, name="index1"),
    
]