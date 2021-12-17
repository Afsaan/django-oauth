from django.contrib import admin
from django.urls import path, include
from authentication.views import *

urlpatterns = [
    path('', home , name = 'home')

]
