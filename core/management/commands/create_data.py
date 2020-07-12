import names
import string
import timeit
from datetime import date, datetime, timedelta
from random import random, choice, randint, randrange, sample
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.fix.data import ARMA, NATUREZA, FACCAO, MODELO, COR, LOREM, CIDADE
from core.management.commands.progress_bar import progressbar
from infracao.models import Arma
from infracao.models import Infracao
from infracao.models import Natureza
from ocorrencia.models import Ocorrencia
from ocorrencia.models import PessoaOcorrencia
from pessoa.models import Comparsa
from pessoa.models import Faccao
from pessoa.models import Pessoa
from pessoa.models import PessoaContato
from pessoa.models import PessoaVeiculo
from veiculo.models import Cor
from veiculo.models import Modelo
from veiculo.models import Veiculo


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


def gen_date(min_year=2019, max_year=datetime.now().year):
    # gera um date no formato yyyy-mm-dd
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random()


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


def gen_text():
    lorem = LOREM.split(' ')
    text = sample(lorem, randint(15, 30))
    return ' '.join(text).title()


def gen_city():
    return choice(CIDADE)


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
            artigo=natureza[0],
            natureza=natureza[1],
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

        address = f'Rua {gen_first_name()} {gen_last_name()}'
        address_number = randint(100, 9999)
        # district = gen_last_name()
        # city = gen_city()
        cep = f'{gen_digits(5)}-{gen_digits(3)}'

        obj = Pessoa(
            nome=nome,
            sobrenome=sobrenome,
            apelido=apelido,
            mae=mae,
            pai=pai,
            faccao=faccao,
            address=address,
            address_number=address_number,
            # district=district,
            # city=city,
            # uf='GO',
            cep=cep,
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
    # Três pra cada pessoa.
    aux = []
    pessoas = Pessoa.objects.all()
    pessoas = progressbar(pessoas, "Comparsas: ")
    for pessoa in pessoas:
        for _ in range(3):
            obj = Comparsa(
                pessoa=pessoa,
                nome=f'{gen_first_name()} {gen_last_name()}',
                rg=gen_rg(),
                cpf=gen_cpf(),
                cnh=gen_digits(6),
            )
            aux.append(obj)
    Comparsa.objects.bulk_create(aux)


QUALIFICACAO = [
    ('aut', 'Autor'),
    ('coaut', 'Co-Autor'),
    ('part', 'Participe'),
    ('vit', 'Vitima')
]

STATUS = [
    ('vivo', 'Vivo'),
    ('morto', 'Morto'),
    ('preso', 'Preso'),
    ('solto', 'Solto')
]


def create_infracao():
    # Infracao
    # Duas pra cada pessoa.
    Infracao.objects.all().delete
    aux = []
    pessoas = Pessoa.objects.all()
    pessoas = progressbar(pessoas, "Infrações: ")
    naturezas = Natureza.objects.all()
    armas = Arma.objects.all()
    for pessoa in pessoas:
        for _ in range(2):
            natureza = choice(naturezas)
            qualificacao = choice(QUALIFICACAO)[0]
            arma = choice(armas)
            status = choice(STATUS)[0]
            obj = Infracao(
                pessoa=pessoa,
                natureza=natureza,
                qualificacao=qualificacao,
                arma=arma,
                status=status,
            )
            aux.append(obj)
    Infracao.objects.bulk_create(aux)


def create_ocorrencia():
    # Ocorrencia
    Ocorrencia.objects.all().delete()
    aux = []
    items = progressbar(range(10), "Ocorrências: ")
    for _ in range(10):
        rai = randint(1000, 9999)
        data_do_fato = gen_date()
        descricao = gen_text()
        obj = Ocorrencia(
            rai=rai,
            data_do_fato=data_do_fato,
            descricao=descricao,
        )
        aux.append(obj)
    Ocorrencia.objects.bulk_create(aux)


def create_pessoaocorrencia():
    # PessoaOcorrencia
    # Três pra cada pessoa.
    PessoaOcorrencia.objects.all().delete
    aux = []
    pessoas = Pessoa.objects.all()
    ocorrencias = Ocorrencia.objects.all()
    pessoas = progressbar(pessoas, "Pessoa Ocorrências: ")
    for pessoa in pessoas:
        for _ in range(3):
            ocorrencia = choice(ocorrencias)
            obj = PessoaOcorrencia(
                pessoa=pessoa,
                ocorrencia=ocorrencia
            )
            aux.append(obj)
    PessoaOcorrencia.objects.bulk_create(aux)


def create_pessoaveiculo():
    # PessoaVeiculo
    # Dois pra cada pessoa.
    PessoaVeiculo.objects.all().delete
    aux = []
    pessoas = Pessoa.objects.all()
    veiculos = Veiculo.objects.all()
    pessoas = progressbar(pessoas, "Pessoa Veiculos: ")
    for pessoa in pessoas:
        for _ in range(2):
            veiculo = choice(veiculos)
            obj = PessoaVeiculo(
                pessoa=pessoa,
                veiculo=veiculo
            )
            aux.append(obj)
    PessoaVeiculo.objects.bulk_create(aux)


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
        create_pessoaveiculo()

        toc = timeit.default_timer()

        msg = 'Dados criados com successo.'
        self.stdout.write(self.style.SUCCESS(msg))

        msg_time = 'Total Time {} s'.format(round(toc - tic, 2))
        self.stdout.write(self.style.WARNING(msg_time))
