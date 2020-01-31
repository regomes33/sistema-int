import names
import string
import timeit
from random import choice, randint, randrange
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


def gen_rg():
    return gen_digits(10)


def gen_cpf():
    def calcula_digito(digs):
        s = 0
        qtd = len(digs)
        for i in range(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10:
            return 0
        return res
    n = [randrange(10) for i in range(9)]
    n.append(calcula_digito(n))
    n.append(calcula_digito(n))
    return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


def gen_phone():
    return f'{gen_digits(2)} {gen_digits(4)}-{gen_digits(4)}'


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
    Infracao.objects.all().delete()
    Pessoa.objects.all().delete()
    aux = []
    _range = range(10)
    items = progressbar(_range, "Pessoas: ")
    for item in items:
        nome = gen_first_name()
        sobrenome = gen_last_name()
        apelido = gen_first_name()
        mae = f'{gen_first_name()} {gen_last_name()}'
        pai = f'{gen_first_name()} {gen_last_name()}'
        faccoes = Faccao.objects.all()
        faccao = choice(faccoes)

        obj = Pessoa(
            nome=nome,
            sobrenome=sobrenome,
            apelido=apelido,
            mae=mae,
            pai=pai,
            faccao=faccao,
            city='Goiânia',
            uf='GO',
            rg=gen_rg(),
            cpf=gen_cpf(),
            cnh=gen_digits(6),
        )
        aux.append(obj)
    Pessoa.objects.bulk_create(aux)


def create_pessoacontato():
    # PessoaContato
    PessoaContato.objects.all().delete()
    aux = []
    pessoas = Pessoa.objects.all()
    pessoas = progressbar(pessoas, "Contatos: ")
    for pessoa in pessoas:
        telefone1 = gen_phone()
        obj1 = PessoaContato(
            pessoa=pessoa,
            telefone=telefone1
        )
        aux.append(obj1)

        telefone2 = gen_phone()
        obj2 = PessoaContato(
            pessoa=pessoa,
            telefone=telefone2
        )
        aux.append(obj2)
    PessoaContato.objects.bulk_create(aux)


def create_comparsa():
    # Comparsa
    aux = []
    pessoas = Pessoa.objects.all()
    pessoas = progressbar(pessoas, "Comparsas: ")
    for pessoa in pessoas:
        for _ in range(3):
            obj = Comparsa(
                pessoa=pessoa,
                nome_comparsa=f'{gen_first_name()} {gen_last_name()}'
            )
            aux.append(obj)
    Comparsa.objects.bulk_create(aux)


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
