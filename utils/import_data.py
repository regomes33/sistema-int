'''
Importa os dados do Cloudinary.
'''
import csv
import io
import pandas as pd
import timeit
import urllib.request
from random import randint
from pprint import pprint
from django.contrib.auth.models import User, Group
from pessoa.models import Faccao
from pessoa.models import Pessoa
from pessoa.models import Foto
from pessoa.models import Comparsa
from ocorrencia.models import Natureza
from ocorrencia.models import Arma
from ocorrencia.models import Ocorrencia
from ocorrencia.models import AreaUpm
from ocorrencia.models import Motivacao
from ocorrencia.models import Infracao
from ocorrencia.models import PessoaOcorrencia
from veiculo.models import Cor
from veiculo.models import Modelo
from veiculo.models import Veiculo


dict_users = {}


def my_import_data():
    tic = timeit.default_timer()

    path = 'https://res.cloudinary.com/sistema-int/raw/upload'

    filename_user = f'{path}/v1588391446/csv/auth_user_c3md4d.csv'
    filename_pessoa_faccao = f'{path}/v1588391160/csv/pessoa_faccao_lb17pd.csv'
    filename_pessoa_pessoa = f'{path}/v1588386442/csv/pessoa_pessoa_ei4ado.csv'
    filename_pessoa_foto = f'{path}/v1588386919/csv/pessoa_foto_vakddv.csv'
    filename_pessoa_comparsa = f'{path}/v1588463742/csv/pessoa_comparsa_q52hvu.csv'
    filename_pessoa_ocorrencia = f'{path}/v1588536338/csv/ocorrencia_pessoaocorrencia_omw4h7.csv'
    filename_natureza = f'{path}/v1588394597/csv/ocorrencia_natureza_z6ytfb.csv'
    filename_arma = f'{path}/v1588394764/csv/ocorrencia_arma_bmfnm9.csv'
    filename_ocorrencia = f'{path}/v1588394853/csv/ocorrencia_ocorrencia_wgacov.csv'
    filename_areaupm = f'{path}/v1588395968/csv/ocorrencia_areaupm_qk84df.csv'
    filename_motivacao = f'{path}/v1588396087/csv/ocorrencia_motivacao_zp5cpb.csv'
    filename_infracao = f'{path}/v1588466176/csv/ocorrencia_infracao_nxg1sl.csv'
    filename_veiculo_cor = f'{path}/v1588385001/csv/veiculo_cor_iq3e7i.csv'
    filename_veiculo_modelo = f'{path}/v1588385550/csv/veiculo_modelo_ury3nj.csv'
    filename_veiculo_veiculo = f'{path}/v1588386054/csv/veiculo_veiculo_bjwhpq.csv'

    dict_pessoas = read_data(filename_user)
    dict_faccao = read_data(filename_pessoa_faccao)

    import_user(filename_user)
    create_data(filename_pessoa_faccao, Faccao)
    create_pessoa(filename_pessoa_pessoa)
    # import_foto(filename_pessoa_foto)
    # import_comparsa(filename_pessoa_comparsa)

    # # Ocorrencia
    # import_ocorrencia(filename_ocorrencia)
    # create_data(filename_natureza, Natureza)
    # create_data(filename_arma, Arma)
    # create_data(filename_areaupm, AreaUpm)
    # create_data(filename_motivacao, Motivacao)
    # import_infracao(filename_infracao)
    # import_pessoa_ocorrencia(filename_pessoa_ocorrencia)

    # # Veiculo
    # create_data(filename_veiculo_cor, Cor)
    # create_data(filename_veiculo_modelo, Modelo)
    # create_data(filename_veiculo_veiculo, Veiculo)

    toc = timeit.default_timer()
    return round(toc - tic, 2)


def read_data(filename):
    '''
    Lê os dados para extrair id e slug e montar um dicionario.
    '''
    df = pd.read_csv(filename)
    df = df[['id', 'slug']]
    dictionary = {}
    for row in df.itertuples():
        dictionary[str(row.id)] = row.slug
    return dictionary


def create_data(filename, model):
    df = pd.read_csv(filename)
    df = df.drop(['id'], axis=1)
    aux = df.T.apply(dict).tolist()
    data = [model(**item) for item in aux]
    model.objects.bulk_create(data)


def csv_online_to_list(url: str) -> list:
    '''
    Lê um CSV a partir de uma url.
    '''
    url_open = urllib.request.urlopen(url)
    reader = csv.DictReader(io.StringIO(
        url_open.read().decode('utf-8')), delimiter=',')
    csv_data = [line for line in reader]
    return csv_data


def create_pessoa(filename):
    items = csv_online_to_list(filename)
    data = []
    for i, item in enumerate(items):
        dict_pessoas[item['id']] = item['slug']
        del item['id']
        if item.get('address_number'):
            item['address_number'] = int(item.get('address_number'))
        else:
            item['address_number'] = None

        if not item.get('cpf'):
            item['cpf'] = None

        if not item.get('cnh'):
            item['cnh'] = None

        if not item.get('cep'):
            item['cep'] = None

        created_by_id = item.get('created_by_id')
        if created_by_id:
            created_by_username = dict_users.get(int(created_by_id))
        else:
            created_by_username = 'admin'
        if created_by_username:
            created_by = User.objects.get(username=created_by_username)
            item['created_by'] = created_by

        faccao_id = item.get('faccao_id')
        if faccao_id:
            faccao = Faccao.objects.get(pk=faccao_id)
            item['faccao'] = faccao

        obj = Pessoa(**item)
        data.append(obj)

    Pessoa.objects.bulk_create(data)


'''
User
'''


def import_user(filename):
    df = pd.read_csv(filename)
    aux = df.T.apply(dict).tolist()
    for item in aux:
        dict_users[item['id']] = item['username']
        del item['id']
        User.objects.create(
            username=item['username'],
            first_name=item['first_name'],
            last_name=item['last_name'],
            email=item['email'],
            is_active=item['is_active'],
            is_staff=item['is_staff'],
            is_superuser=item['is_superuser'],
            password=item['password'],
            date_joined=item['date_joined'],
        )

'''
Pessoa
'''


def import_foto(filename):
    df = pd.read_csv(filename)
    items = df.T.apply(dict).tolist()
    data = []
    for item in items:
        del item['id']
        if isinstance(item.get('foto'), str):
            pessoa_id = item.get('pessoa_id')
            pessoa_slug = dict_pessoas.get(pessoa_id)
            if pessoa_slug:
                pessoa = Pessoa.objects.get(slug=pessoa_slug)
                item['pessoa'] = pessoa

            obj = Foto(**item)
            data.append(obj)

    Foto.objects.bulk_create(data)


def import_tatuagem(filename):
    pass


def import_pessoacontato(filename):
    pass


def import_comparsa(filename):
    df = pd.read_csv(filename)
    items = df.T.apply(dict).tolist()
    data = []
    for item in items:
        del item['id']
        pessoa_id = item.get('pessoa_id')
        pessoa_slug = dict_pessoas.get(str(pessoa_id))
        if pessoa_slug:
            pessoa = Pessoa.objects.get(slug=pessoa_slug)

        if not isinstance(item.get('cpf'), str):
            item['cpf'] = None

        if not item.get('cnh'):
            item['cnh'] = None

        obj = Comparsa(**item)
        data.append(obj)

    Comparsa.objects.bulk_create(data)


def import_pessoaveiculo(filename):
    pass


'''
Ocorrencia
'''


def import_infracao(filename):
    items = csv_online_to_list(filename)
    data = []
    for item in items:
        del item['id']
        created_by_id = item.get('created_by_id')
        if created_by_id:
            created_by = User.objects.get(pk=created_by_id)
            item['created_by'] = created_by
        else:
            item['created_by'] = User.objects.get(username='admin')

        pessoa_id = item.get('pessoa_id')
        pessoa_slug = dict_pessoas.get(str(pessoa_id))
        if pessoa_slug:
            pessoa = Pessoa.objects.get(slug=pessoa_slug)

        natureza_id = item.get('natureza_id')
        if natureza_id:
            natureza = Natureza.objects.get(pk=natureza_id)
            item['natureza'] = natureza

        arma_id = item.get('arma_id')
        if arma_id:
            arma = Arma.objects.get(pk=arma_id)
            item['arma'] = arma

        obj = Infracao(**item)
        data.append(obj)

    Infracao.objects.bulk_create(data)


def import_ocorrencia(filename):
    df = pd.read_csv(filename).fillna({'created_by_id': '1'})
    items = df.T.apply(dict).tolist()
    data = []
    for item in items:
        del item['id']
        created_by_id = item.get('created_by_id')
        if created_by_id:
            created_by = User.objects.get(pk=created_by_id)
            item['created_by'] = created_by
        else:
            item['created_by'] = User.objects.get(username='admin')

        obj = Ocorrencia(**item)
        data.append(obj)

    Ocorrencia.objects.bulk_create(data)


def import_pessoa_ocorrencia(filename):
    items = csv_online_to_list(filename)
    data = []
    for item in items:
        del item['id']
        created_by_id = item.get('created_by_id')
        if created_by_id:
            created_by = User.objects.get(pk=created_by_id)
            item['created_by'] = created_by
        else:
            item['created_by'] = User.objects.get(username='admin')

        pessoa_id = item.get('pessoa_id')
        pessoa_slug = dict_pessoas.get(str(pessoa_id))
        if pessoa_slug:
            pessoa = Pessoa.objects.get(slug=pessoa_slug)

        ocorrencia_id = item.get('ocorrencia_id')
        if ocorrencia_id:
            ocorrencia = Ocorrencia.objects.get(pk=ocorrencia_id)
            item['ocorrencia'] = ocorrencia

        obj = PessoaOcorrencia(**item)
        data.append(obj)

    PessoaOcorrencia.objects.bulk_create(data)


def import_ocorrenciaveiculo(filename):
    pass
