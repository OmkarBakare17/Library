from django.contrib import admin
from django.urls import path
from login.views import signup,home,login
from library.views import *
urlpatterns = [
    path('',home),
    path('signup/',signup),
    path('login/',login),
    path('book/',book),
    path('addbook/',addbook),
    path('booklist/',book_list),
    path('studentview/', studentview),
    path('studentbooklist/', studentview_booklist),
    path('update/<int:bid>',update),
    path('delete/<int:bid>',delete),
]