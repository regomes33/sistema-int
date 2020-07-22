from django.test import TestCase

from infracao.models import Arma, Infracao, Natureza


class TestArma(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'arma',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Arma, field))


class TestNatureza(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'artigo',
            'natureza',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Natureza, field))


class TestInfracao(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'natureza',
            'qualificacao',
            'arma',
            'status',
            'created',
            'modified',
            'created_by',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Infracao, field))
