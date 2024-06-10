from django.urls import path
from .views import signinview,signupview,logoutview,check_username

urlpatterns = [
    path('signinuser',signinview,name="signinuser"),
    path('signupuser',signupview,name='signupuser'),
    path('logoutuser',logoutview,name='logoutuser'),
]