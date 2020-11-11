from django.urls import path
from .views import  home,login,layout,registrar

urlpatterns = [
    path('', home, name='home'),
    path('', login, name='login'),
    path('registrar', registrar, name='registrar'),
]