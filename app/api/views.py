from django.shortcuts import render

# Create your views here.

from api.serializers import FundoImobiliarioSerializer, LavaJatoSerializer
from api.models import FundoImobiliario, LavaJato
from rest_framework import viewsets, permissions

class FundoImobiliarioViewSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all()
    serializer_class = FundoImobiliarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class LavaJatoViewdSet(viewsets.ModelViewSet):
    queryset = LavaJato.objects.all()
    serializer_class = LavaJatoSerializer
    permissions_class = [permissions.IsAuthenticated]
