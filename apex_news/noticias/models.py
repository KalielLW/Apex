from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    
class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)