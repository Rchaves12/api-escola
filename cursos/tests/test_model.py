from django.test import TestCase

from cursos.models import Curso, Avaliacao

# This is the class we want to test. So, we need to import it


class CursoCreate(object):
    def create(self):
        Curso.objects.create(titulo='teste',
                             url='teste.com.br'
                             )


class CursoTestCase(TestCase):

    @classmethod
    def setUp(self):
        CursoCreate.create(self)

    def test_first_name_label(self):
        curso = Curso.objects.get(id=1)
        field_label = curso._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')

    def test_object_curso(self):
        curso = Curso.objects.get(id=1)
        self.assertEquals(curso.titulo, str('teste'))


class AvaliacaoTestCase(TestCase):

    @classmethod
    def setUp(self):
        CursoCreate.create(self)
        curso = Curso.objects.get(id=1)
        Avaliacao.objects.create(curso=curso,
                                 nome='curso',
                                 email='curso@curso.com.br',
                                 comentario='top',
                                 avaliacao=5
                                 )

    def test_first_name_label(self):
        avaliacao = Avaliacao.objects.get(id=1)
        field_label = avaliacao._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_object_avaliacao(self):
        avaliacao = Avaliacao.objects.get(id=1)
        self.assertEquals(avaliacao.nome, str('curso'))
