from django.db import models

# Create your models here.

TYPE = [
    ('DOC','Docente'),
    ('ALU','Alumno'),
]

class MessageBienvenida(models.Model):
    """Model definition for Message."""
    text = models.CharField(max_length = 255, blank = False, null = False)

    class Meta:
        """Meta definition for Message."""
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        """Unicode representation of Message."""
        return self.text


class MessageType(models.Model):
    """Model definition for Message."""
    text = models.CharField(max_length = 255, blank = False, null = False)
    reply = models.CharField(max_length = 255, blank = False, null = False)
    type = models.CharField(max_length = 8, choices = TYPE, null = False, blank = False)

    class Meta:
        """Meta definition for Message."""
        verbose_name = 'messageType'
        verbose_name_plural = 'messagesTypes'

    def __str__(self):
        """Unicode representation of Message."""
        return self.text

