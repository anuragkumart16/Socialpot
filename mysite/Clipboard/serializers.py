from . models import Linkmodel
from rest_framework import serializers

class LinkSerializers(serializers.ModelSerializer):
    class Meta :
        model = Linkmodel
        fields = '__all__'