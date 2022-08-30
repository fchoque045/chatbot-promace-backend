from django.contrib import admin
from .models import MessageBienvenida, MessageType

# Register your models here.
class MessageAdminConfig(admin.ModelAdmin):
    model = MessageBienvenida
    search_fields = ('text',)
    ordering = ('id',)
    # list_display = ('id', 'text', 'step')

class MessageTypeAdminConfig(admin.ModelAdmin):
    model = MessageType
    search_fields = ('text',type)
    ordering = ('id',)

admin.site.register(MessageBienvenida, MessageAdminConfig)
admin.site.register(MessageType, MessageTypeAdminConfig)
