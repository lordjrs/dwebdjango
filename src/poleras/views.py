from django.shortcuts import render, redirect
from .models import Producto
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def login(request):
    context={
        'form':CustomUserForm()
    }
    return render(request, "login.html", context)

def carrito(request):
    context={

    }
    return render(request, "Carrito.html", context)

def home(request):
    context={

    }
    return render(request, "home.html", context)

def layout(request):
    context={

    }
    return render(request, "layout.html", context)

def registrar(request):
    context = {
        'form':CustomUserForm()

    }
    return render(request, 'registration/registrar.html')
