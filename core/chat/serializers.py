from rest_framework import serializers
from core.chat.models import MessageBienvenida, MessageType, TYPE 

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageBienvenida
        fields = '__all__'
    
    def to_representation(self, instance):

        return {
            'id':instance.id,
            'text':instance.text,
            'options': map(lambda x: x[1] , TYPE)
        }

class MessageTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageType
        fields = '__all__'

