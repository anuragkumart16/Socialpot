from django.contrib import admin
from django.urls import path
from Members.views import *
from Members.views import Home
from Clipboard.views import *
from django.conf import settings
from django.conf.urls.static import static
from otphandler.views import otprequest
from Collaboration.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    # for handling api requests
    path('collab',CollaborationAPI.as_view(),name='collab'),
    path('collabmessage',CollabMessageAPI.as_view(),name='collabmessage'),
    path('collabmember',CollabMembersAPI.as_view(),name='collabmembers'),
    path('collabdata',CollabDataAPI.as_view(),name='collabdata'),
    path('members',Member.as_view(),name="createuser"),
    path('otphandler',otprequest.as_view(),name="otp"),
    path('checkusername',checkusername,name='checkusername'),
    path('checkemail',checkemail,name='checkemail'),
    path('userdetails',getuserdetails.as_view(),name = 'getuserdetails'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenrefresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('linkhandler',linkhandler.as_view(),name='linkhandler'),
    path('texthandler',texthandler.as_view(),name='texthandler'),
    path('filehandler',filehandler.as_view(),name ='filehandler'),
    path('getuserdetails',getuserdetails.as_view(),name = 'getuserdetails'),
    path('changepassword',changepassword.as_view(),name='changepassowrd'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
