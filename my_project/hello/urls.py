from django.urls import path

from . views import index 

urlpatterns = [
    path('hello/', index, name="index"),
]
''' path("<str:name>", greet, name="greet"),'''