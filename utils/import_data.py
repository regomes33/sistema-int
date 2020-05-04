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


dict_users = {}

dict_pessoas = read_data(filename_pessoa_pessoa)
dict_faccao = read_data(filename_pessoa_faccao)
dict_ocorrencia = read_data(filename_ocorrencia)
dict_natureza = read_data(filename_natureza)
dict_arma = read_data(filename_arma)
dict_modelo = read_data(filename_veiculo_modelo)
dict_cor = read_data(filename_veiculo_cor)


def my_import_data():
    tic = timeit.default_timer()

    import_user(filename_user)
    create_data(filename_pessoa_faccao, Faccao)
    create_pessoa(filename_pessoa_pessoa)
    import_foto(filename_pessoa_foto)
    import_comparsa(filename_pessoa_comparsa)

    # Ocorrencia
    import_ocorrencia(filename_ocorrencia)
    create_data(filename_natureza, Natureza)
    create_data(filename_arma, Arma)
    create_data(filename_areaupm, AreaUpm)
    create_data(filename_motivacao, Motivacao)
    import_infracao(filename_infracao)
    import_pessoa_ocorrencia(filename_pessoa_ocorrencia)

    # Veiculo
    create_data(filename_veiculo_cor, Cor)
    create_data(filename_veiculo_modelo, Modelo)
    import_veiculo(filename_veiculo_veiculo)

    toc = timeit.default_timer()
    return round(toc - tic, 2)


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

        created_by = get_users(item.get('created_by_id'))
        del item['created_by_id']
        if created_by:
            item['created_by'] = created_by

        faccao_id = item.get('faccao_id')
        faccao_slug = dict_faccao.get(faccao_id)
        if faccao_slug:
            faccao = Faccao.objects.get(slug=faccao_slug)

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


def get_users(created_by_id):
    '''
    Retorna um usuário.
    '''
    if created_by_id:
        created_by_username = dict_users.get(int(created_by_id))
    else:
        created_by_username = 'admin'

    return User.objects.get(username=created_by_username)


def get_pessoa(pessoa_id):
    '''
    Retorna uma pessoa.
    '''
    pessoa_slug = dict_pessoas.get(str(pessoa_id))
    if pessoa_slug:
        pessoa = Pessoa.objects.get(slug=pessoa_slug)
        return pessoa


def get_natureza(natureza_id):
    '''
    Retorna uma natureza.
    '''
    natureza_slug = dict_natureza.get(str(natureza_id))
    if natureza_slug:
        natureza = Natureza.objects.get(slug=natureza_slug)
        return natureza


def get_arma(arma_id):
    '''
    Retorna uma arma.
    '''
    arma_slug = dict_arma.get(str(arma_id))
    if arma_slug:
        arma = Arma.objects.get(slug=arma_slug)
        return arma


def get_modelo(modelo_id):
    '''
    Retorna uma modelo.
    '''
    modelo_slug = dict_modelo.get(str(modelo_id))
    if modelo_slug:
        modelo = Modelo.objects.get(slug=modelo_slug)
        return modelo


def get_cor(cor_id):
    '''
    Retorna uma cor.
    '''
    cor_slug = dict_cor.get(str(cor_id))
    if cor_slug:
        cor = Cor.objects.get(slug=cor_slug)
        return cor


def import_foto(filename):
    df = pd.read_csv(filename)
    items = df.T.apply(dict).tolist()
    data = []
    for i, item in enumerate(items):
        del item['id']
        if isinstance(item.get('foto'), str):
            pessoa = get_pessoa(item.get('pessoa_id'))
            del item['pessoa_id']
            if pessoa:
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
        pessoa = get_pessoa(item.get('pessoa_id'))
        del item['pessoa_id']
        if pessoa:
            item['pessoa'] = pessoa

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
        created_by = get_users(item.get('created_by_id'))
        del item['created_by_id']
        if created_by:
            item['created_by'] = created_by

        pessoa = get_pessoa(item.get('pessoa_id'))
        del item['pessoa_id']
        if pessoa:
            item['pessoa'] = pessoa

        natureza = get_natureza(item.get('natureza_id'))
        del item['natureza_id']
        if natureza:
            item['natureza'] = natureza

        arma = get_arma(item.get('arma_id'))
        del item['arma_id']
        if arma:
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
        created_by = get_users(item.get('created_by_id'))
        del item['created_by_id']
        if created_by:
            item['created_by'] = created_by

        obj = Ocorrencia(**item)
        data.append(obj)

    Ocorrencia.objects.bulk_create(data)


def import_pessoa_ocorrencia(filename):
    items = csv_online_to_list(filename)
    data = []
    for item in items:
        del item['id']
        created_by = get_users(item.get('created_by_id'))
        del item['created_by_id']
        if created_by:
            item['created_by'] = created_by

        pessoa = get_pessoa(item.get('pessoa_id'))
        del item['pessoa_id']
        if pessoa:
            item['pessoa'] = pessoa

        ocorrencia_id = item.get('ocorrencia_id')
        ocorrencia_slug = dict_ocorrencia.get(ocorrencia_id)
        if ocorrencia_slug:
            ocorrencia = Ocorrencia.objects.get(slug=ocorrencia_slug)

        obj = PessoaOcorrencia(**item)
        data.append(obj)

    PessoaOcorrencia.objects.bulk_create(data)


def import_ocorrenciaveiculo(filename):
    pass


def import_veiculo(filename):
    # placa
    # modelo
    # cor
    # observacao

    df = pd.read_csv(filename)
    items = df.T.apply(dict).tolist()
    data = []
    for i, item in enumerate(items):
        del item['id']

        modelo = get_modelo(item.get('modelo_id'))
        del item['modelo_id']
        if modelo:
            item['modelo'] = modelo

        cor = get_cor(item.get('cor_id'))
        del item['cor_id']
        if cor:
            item['cor'] = cor

        obj = Veiculo(**item)
        data.append(obj)

    Veiculo.objects.bulk_create(data)
