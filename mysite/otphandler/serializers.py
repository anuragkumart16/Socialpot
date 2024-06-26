from rest_framework import serializers


class OtprequestSerializer(serializers.Serializer):
    email = serializers.EmailField()