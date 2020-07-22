from django.test import TestCase

from homicidio.models import AreaUpm, Autoria, Genero, Homicidio, Motivacao


class TestAreaUpm(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'area_upm',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(AreaUpm, field))


class TestAutoria(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'autoria',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Autoria, field))


class TestGenero(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'genero',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Genero, field))


class TestMotivacao(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'titulo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Motivacao, field))


class TestHomicidio(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'rai',
            'data_do_homicidio',
            'forma',
            'area_upm',
            'autoria',
            'genero',
            'vitima',
            'instrumento',
            'motivacao',
            'address',
            'address_number',
            'complement',
            'district',
            'cep',
            'country',
            'created_by',
            'created',
            'modified',

        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Homicidio, field))
