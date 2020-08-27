from django.test import TestCase

from pessoa.models import (
    Comparsa,
    Faccao,
    Foto,
    Pessoa,
    PessoaComparsa,
    PessoaContato,
    PessoaVeiculo,
    Tatuagem
)


class TestPessoa(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'nome',
            'sobrenome',
            'apelido',
            'mae',
            'pai',
            'observacao',
            'faccao',
            'status_atual',
            'vitima',
            'nascimento',
            'created',
            'modified',
            'created_by',
            'address',
            'address_number',
            'complement',
            'district',
            'cep',
            'city',
            'uf',
            'country',
            'cpf',
            'rg',
            'cnh',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Pessoa, field))


class TestFoto(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'foto',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Foto, field))


class TestTatuagem(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'foto',
            'descricao',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Tatuagem, field))


class TestPessoaContato(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'tipo',
            'telefone',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PessoaContato, field))


class TestComparsa(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'nome',
            'cpf',
            'rg',
            'cnh',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Comparsa, field))


class TestPessoaComparsa(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'comparsa',
            'parente',
            'grau_parentesco',
            'observacao',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PessoaComparsa, field))


class TestFaccao(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'nome',
            'funcao',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Faccao, field))


class TestPessoaVeiculo(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'slug',
            'pessoa',
            'veiculo',
            'created_by',
            'created',
            'modified',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PessoaVeiculo, field))
