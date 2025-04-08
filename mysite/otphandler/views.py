from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import random
from .serializers import OtprequestSerializer


class otprequest(APIView):
    def post(self, request):
        serializer = OtprequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"status": False, "message": "Invalid data"},
                status.HTTP_400_BAD_REQUEST,
            )

        email = serializer.validated_data["email"]
        otp = random.randint(1000, 9999)

        subject = "Verify Otp for Across Device"
        message = f"""
Hello,

Your OTP for verifying your email on Across Device is: {otp}

If you didn’t request this, please ignore the email.

Thank you,
Across Device Team
"""
        send_mail(
            subject,
            message,
            "acrossdevice01@gmail.com",  # From email
            [email],  # To email list
            fail_silently=False,
        )

        return Response(
            {"status": True, "message": "OTP sent successfully", "otp": otp},
            status.HTTP_200_OK,
        )
