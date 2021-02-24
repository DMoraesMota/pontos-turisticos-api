from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):

    serializer_class = PontoTuristicoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'endereco__linha1']
    lookup_field = 'nome'
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            """O valor __iexact no nome é para ele não levar em consideração campos maiusculos ou minusculos"""
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o metodo get full'})

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o método get para um id especifico'})

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o método POST para um id especifico'})

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o método DELETE para um id especifico'})

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o PUT get para um id especifico'})

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(self, request, *args, **kwargs)
        # return Response({'hello : sobrescrevendo o PATCH get para um id especifico'})

    """
        Podemos criar a action para criar um recurso específico para o nosos objeto que não se enquadre em nenhum dos outros verbos.
        a chamada é o nome do recurso pontoTuristico/denunciar
        
        no caso eu passei detail = True isto significa que eu preciso passar o ID do recusro q quero manusear 
    """
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    """
        Action onde não preciso passar o id na requisição
        
        no caso uma action geral para o end-point, não necessário passar o PK
    """
    @action(methods=['get'], detail=False)
    def recursoParaOEndPoint(self, request):
        pass


