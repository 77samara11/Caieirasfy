from rest_framework import serializers
from truco.models import Truco
# Create your views here.

class TrucoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truco
        fields = ('id', 'nome_music', 'artista','genero_music', 'link_music')