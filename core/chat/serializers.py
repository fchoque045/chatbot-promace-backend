from rest_framework import serializers
from core.chat.models import Generico, Categoria, Pregunta


class GenericoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Generico
        fields = '__all__'
    
    # def to_representation(self, instance):

    #     return {
    #         'id':instance.id,
    #         'text':instance.text,
    #         'type': map(lambda x: x[1] , TYPE)
    #     }

class CaterogiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregunta
        exclude = ('categoria',)