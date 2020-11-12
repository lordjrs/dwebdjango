from django.urls import path
from .views import home,login_user,layout,registrar

urlpatterns = [
    path('', home, name='home'),
    path('', login_user, name='login_user'),
    path('registrar', registrar, name='registrar'),
]