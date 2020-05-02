from django.test import TestCase
from ocorrencia.models import AreaUpm
from ocorrencia.models import Arma
from ocorrencia.models import Autoria
from ocorrencia.models import Genero
from ocorrencia.models import Homicidio
from ocorrencia.models import Infracao
from ocorrencia.models import Motivacao
from ocorrencia.models import Natureza
from ocorrencia.models import Ocorrencia
from ocorrencia.models import OcorrenciaVeiculo
from ocorrencia.models import PessoaOcorrencia


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


class TestArma(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'arma',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Arma, field))


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


class TestOcorrencia(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'rai',
            'data_do_fato',
            'descricao',
            'created',
            'modified',
            'created_by',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Ocorrencia, field))


class TestPessoaOcorrencia(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'ocorrencia',
            'created',
            'modified',
            'created_by',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PessoaOcorrencia, field))


class TestOcorrenciaVeiculo(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'ocorrencia',
            'veiculo',
            'created',
            'modified',
            'created_by',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(OcorrenciaVeiculo, field))


class TestAreaUpm(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'area_upm',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(AreaUpm, field))


class TestMotivacao(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'titulo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Motivacao, field))


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
            'city',
            'uf',
            'cep',
            'country',
            'created_by',
            'created',
            'modified',

        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Homicidio, field))
