from rest_framework import serializers
from django.contrib.auth.models import User

class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','id','email']




