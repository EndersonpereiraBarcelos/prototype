from rest_framework import serializers
from api.models import FundoImobiliario,LavaJato


class FundoImobiliarioSerializer(serializers.ModelSerializer):
  class Meta:
    model = FundoImobiliario
    fields = [
      'codigo',
      'setor',
      'dividend_yield_medio_12m',
      'vacancia_financeira',
      'vacancia_fisica',
      'quantidade_ativos'
    ]

class LavaJatoSerializer(serializers.ModelSerializer):
  class Meta:
    model = LavaJato
    fields = [
      'Nome',
      'Serviço',
      'Funcionario'
    ]