from django.test import TestCase

from ocorrencia.models import Ocorrencia, OcorrenciaVeiculo, PessoaOcorrencia


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
