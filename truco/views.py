from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from truco.models import Truco
from .serializers import TrucoSerializer

class TrucoViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_field = ['^nome_music', '@artista', '=genero_music', '^link_music']
    queryset = Truco.objects.all()
    serializer_class = TrucoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes =(TokenAuthentication,)
