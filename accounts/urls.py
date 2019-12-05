from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('users/', views.users, name="users"),
    path('sendsms/', views.sendsms, name='sendsms'),
    path('patient/', views.patient, name='patient'),
    path('edit/<int:user_id>', views.edit, name='edit'),
    path('delete/<int:user_id>', views.delete, name='delete'),
]
