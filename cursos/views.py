from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    """
        API de Curso
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """API Avaliação"""
    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        serializer = CursoSerializer(avaliacao, many=True)
        return Response(serializer.data)
