import json
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from config.settings import BASE_DIR

from core.chat.models import MessageBienvenida, MessageType
from core.chat.serializers import MessageSerializer, MessageTypeSerializer

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

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageBienvenida.objects.all()
    serializer_class = MessageSerializer

    # def get(self, request, format=None):
    #     return Response("test")
    
    # def list(self,request):
    #     print('mensajes')
    #     message_serializer = self.get_serializer(self.get_queryset(),many = True)
    #     return Response(message_serializer.data, status = status.HTTP_200_OK)


class MessageListAPIView(ListAPIView):
    queryset = MessageBienvenida.objects.all()
    serializer_class = MessageSerializer

class MessageTypeListAPIView(ListAPIView):
    queryset = MessageType.objects.all()
    serializer_class = MessageTypeSerializer

    def get_queryset(self, type=None):
        print('en get_queryset', type[0])
        if type is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(type=type[0])

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset(type=args))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        type = request.data['type']
        return self.list(request, type, **kwargs)