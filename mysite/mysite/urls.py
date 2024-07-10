
from django.contrib import admin
from django.urls import path,include
from Members.views import home,checkusername,checkemail, getuserdetails
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
    path('otphandler',otprequest.as_view(),name="otp"),
    path('checkusername',checkusername,name='checkusername'),
    path('checkemail',checkemail,name='checkemail'),
    path('userdetails',getuserdetails.as_view(),name = 'getuserdetails'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenrefresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('linkhandler',linkhandler.as_view(),name='linkhandler'),
    path('texthandler',texthandler.as_view(),name='texthandler'),
    path('filehandler',filehandler.as_view(),name ='filehandler'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
