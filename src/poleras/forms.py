from django import forms
from django.forms import ModelForm
from .models import Pedido, Producto
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'password1', 'password2', 'email']
