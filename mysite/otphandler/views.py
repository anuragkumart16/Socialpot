from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .serializers import OtprequestSerializer

# Create your views here.

class otprequest(APIView):
    
    def post(self,request):
        # getting the data needed
        data = request.data
        print(data)
        serializer = OtprequestSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message' : 'something went wrong and its from frontend'
            },status.HTTP_400_BAD_REQUEST)
        
        email = data['email']
        global otp
        otp= random.randint(0000,9999)

        # Email account credentials
        from_address = "acrossdevice01@gmail.com"
        password = "bapw oify vutv fuau"

        # send email to 
        to_address = email

        # Email content
        subject = "Verify Otp for Across Device"
        body = f"your otp for email verification is {otp} ."

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Create server object with SSL option
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()

        return Response({
            'status':True,
            'message':'otp succesfully sent',
            'otp': f'{otp}'
        },status.HTTP_200_OK)




        


