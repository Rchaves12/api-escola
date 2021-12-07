from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CursoAPIView,
    CursosAPIView,
    AvaliacaoAPIView,
    AvaliacoesAPIView,
    CursoViewSet,
    AvaliazaoViewSet)

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliazaoViewSet)

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),

    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]
