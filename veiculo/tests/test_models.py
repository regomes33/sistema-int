from django.test import TestCase
from veiculo.models import Veiculo
from veiculo.models import Modelo
from veiculo.models import Cor


class TestVeiculo(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'placa',
            'modelo',
            'cor',
            'observacao',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Veiculo, field))


class TestModelo(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'modelo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Modelo, field))


class TestCor(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'cor',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Cor, field))
