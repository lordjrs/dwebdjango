from django.shortcuts import render

# Create your views here.

def about(request):
    context={

    }
    return render(request, "about.html", context)

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

def register(request):
    context={

    }
    return render(request, "register.html", context)