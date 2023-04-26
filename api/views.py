from django.shortcuts import render

# Create your views here.
from api.serializers import FundoImobiliarioSerializer, LavaJatoSerializer
from rest_framework import viewsets, permissions
from api.models import FundoImobiliario, LavaJato


class FundoImobiliarioViewSet(viewsets.ModelViewSet):
  queryset = FundoImobiliario.objects.all()
  serializer_class = FundoImobiliarioSerializer
  permission_classes = [permissions.IsAuthenticated]


class LavaJatoViewSet(viewsets.ModelViewSet):
  queryset = LavaJato.objects.all()
  serializer_class = LavaJatoSerializer
  permission_classes = [permissions.IsAuthenticated]
