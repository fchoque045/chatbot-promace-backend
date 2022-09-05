from ast import Try
import json
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from config.settings import BASE_DIR

from core.chat.models import Generico, Categoria, Pregunta
from core.chat.serializers import GenericoSerializer, CaterogiaSerializer, PreguntaSerializer

@api_view(('POST',))
def get_response(request):

    with open(os.path.join(BASE_DIR, 'core/flow/initial.json'), encoding='utf-8') as f:
        data = json.load(f)

    message = request.data['message']
    data = {'response': message + ' como estas'}
    return Response(data, status = status.HTTP_200_OK)

def get_response(request):
    return Response({'response': 'como estas'}, status = status.HTTP_200_OK) 


# class MessageViewSet(viewsets.GenericViewSet):
#     model = Message
#     serializer_class = MessageSerializer

#     # def get_queryset(self):
#     #     return self.get_serializer().Meta.model.objects.filter(state = True)
    
#     def list(self, request):
#         data = self.get_queryset()
#         data = self.get_serializer(data, many = True)
#         return Response(data.data)

class GenericoViewSet(viewsets.ModelViewSet):
    queryset = Generico.objects.all()
    serializer_class = GenericoSerializer

    # def get(self, request, format=None):
    #     return Response("test")
    
    # def list(self,request):
    #     print('mensajes')
    #     message_serializer = self.get_serializer(self.get_queryset(),many = True)
    #     return Response(message_serializer.data, status = status.HTTP_200_OK)


class GenericoListAPIView(ListAPIView):
    queryset = Generico.objects.all()
    serializer_class = GenericoSerializer

    def get_queryset(self, **kwargs):
        try: 
            return self.get_serializer().Meta.model.objects.filter(type=kwargs['type'])
        except: 
            return self.get_serializer().Meta.model.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset(type=kwargs['type']))
        except:
            queryset = self.filter_queryset(self.get_queryset())        

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        type = request.GET.get('type')
        if type is None:
            return self.list(request, *args, **kwargs)
        return self.list(request, type=type)

class CategoriaListAPIView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CaterogiaSerializer
    
    def get(self, request, *args, **kwargs):
        print('hola desde get')
        return Response({'message': 12}, status=status.HTTP_201_CREATED)



class PreguntaListAPIView(ListAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

    def get_queryset(self, **kwargs):
        if kwargs is None:
            return self.get_serializer().Meta.model.objects.all()
        id_category = Categoria.objects.get(nombre_corto=kwargs['category'])
        return self.get_serializer().Meta.model.objects.filter(categoria=id_category)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(category=kwargs['category']))        

        serializer = self.get_serializer(queryset, many=True)
        print({'body':serializer.data})
        return Response({'body':serializer.data})

    def post(self, request, *args, **kwargs):        
        category = request.data['categoria']
        return self.list(request,category=category)