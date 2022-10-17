from rest_framework import viewsets

from .serializers import NoticiaSerializer, AutorSerializer, CategoriaSerializer

from .models import Noticia, Autor, Categoria

class NoticiasViewSet(viewsets.ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    http_method_names = ['get', 'post', 'put', 'path', 'delete']
    
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    http_method_names = ['get', 'post', 'put', 'path']