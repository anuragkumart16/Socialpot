from django.urls import path
from Clipboard.views import apilink,apitext

urlpatterns = [
    path('apilink/',apilink),
    path('apitext',apitext),
]
