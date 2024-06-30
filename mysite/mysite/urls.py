"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Members.views import home , usercreationapi,checkusername,checkemail
from Clipboard.views import *
from django.conf import settings
from django.conf.urls.static import static
from otphandler.views import otprequest
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('members/',include("Members.urls")),
    path('clipboard',clipboard,name="clipboard"),
    path('textholder',textholder,name="textholder"),
    path('fileholder',fileholder,name="fileholder"),
    path('linkholder',linkholder,name="linkholder"),
    path('viewclipboard',viewclipboard,name='viewclipboard'),
    path('delitems',delitems,name='delitems'),
    
    # for handling api requests
    path('api/',include('api.urls')),
    path('otphandler',otprequest.as_view(),name="otp"),
    path('checkusername',checkusername,name='checkusername'),
    path('checkemail',checkemail,name='checkemail'),
    path('createuser',usercreationapi.as_view(),name='createuser'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenrefresh', TokenRefreshView.as_view(), name='token_refresh'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
