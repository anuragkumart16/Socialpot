from django.urls import path
from .views import signinview,signupview,logoutview

urlpatterns = [
    path('signinuser',signinview,name="signinuser"),
    path('signupuser',signupview,name='signupuser'),
    path('logoutuser',logoutview,name='logoutuser'),
]