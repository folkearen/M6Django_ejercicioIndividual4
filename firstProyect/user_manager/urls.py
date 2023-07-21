from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'user_manager'

urlpatterns = [
    # path('', mostrarUsuarios, name='mostrarUsuarios'),
    path('signUp/', signUp, name='signUp'),
    path('signUp/successful/', successfulRegistration, name='successfulRegistration')
]
