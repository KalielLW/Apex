from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from noticias.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register('noticias', NoticiasViewSet, basename='noticias')
router.register('autor', AutorViewSet, basename='autor')
router.register('categoria', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]