from django.urls import path
from Clipboard.views import apilink

urlpatterns = [
    path('apilink/',apilink),
]
