from django import forms
from django.forms import ModelForm
from .models import Pedido, Producto
import datetime
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    pass