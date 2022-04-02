from ast import pattern
from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	
    path('addBook', views.addBook), 
    path('view/<int:id>', views.viewBook), 
    path('author', views.addAuthorBook), 
    path('book', views.addBookAuthor), 
    path('authors', views.authors), 
    path('addAuthor', views.addAuthor), 
    path('view/author/<int:id>', views.viewAuthor)
]
