# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('patient-profile/', views.patient_profile, name='patient_profile'),
    path('doctor-profile/', views.doctor_profile, name='doctor_profile'),
    path('logout/', views.user_logout, name='logout'),
]
