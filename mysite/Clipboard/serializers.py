from . models import Linkmodel,Textmodel,Filemodel
from rest_framework import serializers

class LinkSerializers(serializers.Serializer):
    Link = serializers.CharField()
    
class AnotherLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Linkmodel
        fields = '__all__'

class TextSerializers(serializers.Serializer):
    Text = serializers.CharField()

class AnotherTextSerializers(serializers.ModelSerializer):
    class Meta:
        model = Textmodel
        fields = '__all__'

class FileSerializers(serializers.ModelSerializer):
    class Meta :
        model = Filemodel
        fields = '__all__'

class AnotherFileSerializers(serializers.Serializer):
    File= serializers.FileField()
    Filename = serializers.CharField()