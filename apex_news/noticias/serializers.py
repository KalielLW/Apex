from urllib import response
from rest_framework import serializers
from .models import Categoria, Autor, Noticia

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']
        
class AutorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autor
        fields = ['id', 'nome', 'descricao']
        
class NoticiaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Noticia
        fields = ['id', 'titulo', 'text', 'autor', 'categoria']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['autor'] = AutorSerializer(instance.autor).data
        response['Categoria'] = CategoriaSerializer(instance.categoria).data
        return response