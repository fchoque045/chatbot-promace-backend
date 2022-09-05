from django.contrib import admin
from .models import Generico, Categoria, Pregunta

# Register your models here.
class GenericoAdminConfig(admin.ModelAdmin):
    model = Generico
    search_fields = ('text', 'type')
    ordering = ('id',)
    list_display = ('id', 'text', 'type' )

class CategoriaAdminConfig(admin.ModelAdmin):
    model = Categoria
    search_fields = ('descripcion','nombre_corto')
    ordering = ('id',)
    list_display = ('id', 'descripcion', 'nombre_corto' )

class PreguntaAdminConfig(admin.ModelAdmin):
    model = Pregunta
    search_fields = ('text', 'respuesta', 'categoria')
    list_display = ('id', 'text', 'respuesta', 'categoria')
    ordering = ('id',)

admin.site.register(Generico, GenericoAdminConfig)
admin.site.register(Categoria, CategoriaAdminConfig)
admin.site.register(Pregunta, PreguntaAdminConfig)
