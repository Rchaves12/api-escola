from django.test import TestCase

from cursos.models import Curso

# This is the class we want to test. So, we need to import it


class CursoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Curso.objects.create(titulo='teste', url='teste.com.br')

    def test_first_name_label(self):
        author = Curso.objects.get(id=1)
        field_label = author._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')

    def test_object_curso(self):
        curso = Curso.objects.get(id=1)
        self.assertEquals(curso.titulo, str('teste'))
