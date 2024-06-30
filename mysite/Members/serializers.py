from rest_framework import serializers
from django.contrib.auth.models import User

class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField()

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class RegisterSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def create(self,validated_data):
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    



