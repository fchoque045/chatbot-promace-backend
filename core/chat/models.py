from django.db import models

# Create your models here.

# CATEGORY = [
#     ('DCAP', 'Docente que cursaron año pasado'),
#     ('IC',	'Incripcion al campus'),
#     ('IC',	'Inicio cursado'),
#     ('CD',	'Carga de datos'),
# ]

TYPE = [
    ('MBie', 'Mensaje Bienvenida'),
    ('MDes', 'Mensaje Despedida'),
    ('MErr', 'Mensaje Error'),
    ('MDef', 'Mensaje Default'),
]

class Generico(models.Model):
    """Model definition for Generico."""
    text = models.CharField(max_length = 255, blank = False, null = False)
    type = models.CharField(max_length = 25, choices = TYPE)

    class Meta:
        """Meta definition for Generico."""
        verbose_name = 'generico'
        verbose_name_plural = 'genericos'

    def __str__(self):
        """Unicode representation of Generico."""
        return self.type


class Categoria(models.Model):
    """Model definition for Categoria."""
    descripcion = models.CharField(max_length = 255, blank = False, null = False)
    nombre_corto = models.CharField(max_length = 10, blank = False, null = False)

    class Meta:
        """Meta definition for Categoria."""
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre_corto

class Pregunta(models.Model):
    """Model definition for Pregunta."""
    text = models.CharField(max_length = 255, blank = False, null = False)    
    respuesta = models.CharField(max_length = 255, blank = False, null = False)    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = False)

    class Meta:
        """Meta definition for Pregunta."""
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'

    def __str__(self):
        """Unicode representation of Pregunta."""
        return self.text