from django.urls import path, include
from . import views
from . views import index2

urlpatterns = [
    path('book/', index2, name="index2"),
     path('html5/links', views.links, name='links'),
    path('html5/text/formatting', views.formatting, name='formatting'),
    path('html5/listing', views.listing, name='listing'),
    path('html5/tables', views.tables, name='tables'),
    path('book/search', views.search_books, name='search_books'),
    path('lab8', views.lab8_tasks, name='lab8_tasks'),
    path('listbooks/', views.list_books, name='list_books'),
    path('addbook/', views.add_book, name='add_book'),
    path('editbook/<int:id>/', views.edit_book, name='edit_book'),
    path('deletebook/<int:id>/', views.delete_book, name='delete_book'),
]

