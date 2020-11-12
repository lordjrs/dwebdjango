from django.urls import path
from .views import home,login_user,layout,registrar,carrito

urlpatterns = [
    path('', home, name='home'),
    path('', login_user, name='login_user'),
    path('registrar', registrar, name='registrar'),
    path('comprar', carrito, name='comprar')
]