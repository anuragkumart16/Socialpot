from . models import Linkmodel,Textmodel,Filemodel
from rest_framework import serializers

class LinkSerializers(serializers.ModelSerializer):
    class Meta :
        model = Linkmodel
        fields = '__all__'

class TextSerializers(serializers.ModelSerializer):
    class Meta :
        model = Textmodel
        fields = '__all__'

class FileSerializers(serializers.ModelSerializer):
    class Meta :
        model = Filemodel
        fields = '__all__'