from django.urls import path
from .views import home,about,register,layout

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('register', register, name='register')
]