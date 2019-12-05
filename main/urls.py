from django.urls import path, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('patients/', views.patients, name='patients'),
    path('rights/', views.rights, name="rights"),
]
