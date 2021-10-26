from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(generics.ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoAPIView(generics.ListAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
