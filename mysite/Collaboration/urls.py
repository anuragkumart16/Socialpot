from django.urls import path,include
from .views import *


urlpatterns = [
    path('collabapi',CollaborationAPI.as_view(),name='collabapi'),
]
