from django.urls import path, include
from .views import home,login_user,layout,registrar,carrito,listado_poleras

urlpatterns = [
    path('', home, name='home'),
    path('', login_user, name='login_user'),
    path('registrar', registrar, name='registrar'),
    path('comprar', carrito, name='comprar'),
    path('listado-poleras', listado_poleras, name="listado_poleras"),
    path('oauth/', include('social_django.urls', namespace='social')),
]