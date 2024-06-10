from django.urls import path
from .views import signinview,signupview,logoutview,changepassword

urlpatterns = [
    path('signinuser',signinview,name="signinuser"),
    path('signupuser',signupview,name='signupuser'),
    path('logoutuser',logoutview,name='logoutuser'),
    path('changepassword',changepassword,name="changepassword")
]