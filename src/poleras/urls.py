from django.urls import path
from .views import home,login_user,layout,registrar,carrito,listado_poleras

urlpatterns = [
    path('', home, name='home'),
    path('', login_user, name='login_user'),
    path('registrar', registrar, name='registrar'),
    path('comprar', carrito, name='comprar'),
    path('listado-poleras', listado_poleras, name="listado_poleras"),
]