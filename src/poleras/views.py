from django.shortcuts import render, redirect
from .models import Producto
from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
# Create your views here.

def login_user(request):
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

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, 'registration/registrar.html',context)
