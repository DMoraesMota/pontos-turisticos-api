from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from avaliacoes.api.viewsets import AvaliacaoViewSet
from comentarios.api.viewsets import ComentarioViewSet
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet
from enderecos.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()
router.register(r'pontoTuristico', PontoTuristicoViewSet, basename='pontoTuristico')
router.register(r'atracao', AtracaoViewSet, basename='atracao')
router.register(r'endereco', EnderecoViewSet, basename='endereco')
router.register(r'comentario', ComentarioViewSet, basename='comentario')
router.register(r'avaliacao', AvaliacaoViewSet, basename='avaliacao')

urlpatterns = [
    path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
