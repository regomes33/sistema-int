# import names
import string
import timeit
from random import choice, randint
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from pessoa.models import Pessoa
from pessoa.models import PessoaFoto
from pessoa.models import PessoaContato
from pessoa.models import Comparsa
from pessoa.models import Tatuagem
from pessoa.models import Natureza
from pessoa.models import Arma
from pessoa.models import Infracao
from pessoa.models import Faccao
from pessoa.models import Ocorrencia
from pessoa.models import PessoaOcorrencia
from pessoa.models import Veiculo
from pessoa.models import Modelo
from pessoa.models import Cor
from core.management.commands.progress_bar import progressbar
from core.fix.data import ARMA, NATUREZA, FACCAO, MODELO, COR


def gen_string(max_length):
    return str(''.join(choice(string.ascii_letters) for i in range(max_length)))
gen_string.required = ['max_length']


def gen_digits(max_length: int):
    '''Gera dígitos numéricos.'''
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_first_name():
    return names.get_first_name()


def gen_last_name():
    return names.get_last_name()


def gen_email(first_name: str, last_name: str, company: str = None):
    EMAIL = ('email', 'gmail', 'yahoo', 'hotmail', 'uol')
    first_name = slugify(first_name)
    last_name = slugify(last_name)
    email = '{}.{}@{}.com'.format(first_name, last_name, sufix)
    return email


def create_modelo():
    # Modelo
    Veiculo.objects.all().delete()
    Modelo.objects.all().delete()
    aux = []
    _modelos = MODELO
    modelos = progressbar(_modelos, "Modelos: ")
    for modelo in modelos:
        obj = Modelo(
            modelo=modelo,
        )
        aux.append(obj)
    Modelo.objects.bulk_create(aux)


def create_cor():
    # Cor
    Cor.objects.all().delete()
    aux = []
    _cores = COR
    cores = progressbar(_cores, "Cores: ")
    for cor in cores:
        obj = Cor(
            cor=cor,
        )
        aux.append(obj)
    Cor.objects.bulk_create(aux)


def create_veiculo():
    # Veiculo
    aux = []
    _range = range(10)
    items = progressbar(_range, "Veiculos: ")
    for item in items:
        placa = f'{gen_string(3).upper()}-{str(randint(1,9999)).zfill(4)}'

        modelos = Modelo.objects.all()
        modelo = choice(modelos)

        cores = Cor.objects.all()
        cor = choice(cores)

        obj = Veiculo(
            placa=placa,
            modelo=modelo,
            cor=cor,
        )
        aux.append(obj)
    Veiculo.objects.bulk_create(aux)


def create_arma():
    # Arma
    Arma.objects.all().delete()
    aux = []
    _armas = ARMA
    armas = progressbar(_armas, "Armas: ")
    for arma in armas:
        obj = Arma(
            arma=arma,
        )
        aux.append(obj)
    Arma.objects.bulk_create(aux)


def create_natureza():
    # Natureza
    Natureza.objects.all().delete()
    aux = []
    _naturezas = NATUREZA
    naturezas = progressbar(_naturezas, "Naturezas: ")
    for natureza in naturezas:
        obj = Natureza(
            natureza=natureza,
        )
        aux.append(obj)
    Natureza.objects.bulk_create(aux)


def create_faccao():
    # Faccao
    Faccao.objects.all().delete()
    aux = []
    _faccoes = FACCAO
    faccoes = progressbar(_faccoes, "Facções: ")
    for faccao in faccoes:
        obj = Faccao(
            nome=faccao,
        )
        aux.append(obj)
    Faccao.objects.bulk_create(aux)


def create_pessoa():
    # Pessoa
    pass


def create_pessoacontato():
    # PessoaContato
    pass


def create_comparsa():
    # Comparsa
    pass


def create_infracao():
    # Infracao
    pass


def create_ocorrencia():
    # Ocorrencia
    pass


def create_pessoaocorrencia():
    # PessoaOcorrencia
    pass


class Command(BaseCommand):
    help = ''' Cria dados iniciais para o projeto. '''

    def handle(self, *args, **kwargs):
        tic = timeit.default_timer()

        create_modelo()
        create_cor()
        create_veiculo()
        create_arma()
        create_natureza()
        create_faccao()
        create_pessoa()
        create_pessoacontato()
        create_comparsa()
        create_infracao()
        create_ocorrencia()
        create_pessoaocorrencia()

        toc = timeit.default_timer()

        msg = 'Dados criados com successo.'
        self.stdout.write(self.style.SUCCESS(msg))

        msg_time = 'Total Time {} s'.format(round(toc - tic, 2))
        self.stdout.write(self.style.WARNING(msg_time))
