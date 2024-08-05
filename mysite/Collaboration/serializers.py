from rest_framework import serializers
from .models import *

# CollaborationSerializer
class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = '__all__'

# CollabMembersSerializer
class CollabMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollabMembers
        fields = '__all__'

# CollabDataSerializer
class CollabDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollabData
        fields = '__all__'

# CollabMessagesSerializer
class CollabMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollabMessages
        fields = '__all__'