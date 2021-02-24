from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico

class PontoTuristicoSerializer(ModelSerializer):

    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()

    """
        Criando mais um campo para mostrar no serializer 
    """
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','foto', 'aprovado', 'atracoes', 'comentarios', 'avaliacoes', 'endereco', 'descricao_completa' , 'descricao_completa2')

    """
        Criando mais um campo para mostrar no serializer 
    """
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
