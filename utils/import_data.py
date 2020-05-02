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
from veiculo.models import Cor
from veiculo.models import Modelo
from veiculo.models import Veiculo


def my_import_data():
    tic = timeit.default_timer()

    path = 'https://res.cloudinary.com/sistema-int/raw/upload'

    filename_user = 'https://res.cloudinary.com/sistema-int/raw/upload/v1588391446/csv/auth_user_c3md4d.csv'
    import_user(filename_user)

    # filename_veiculo_cor = f'{path}/v1588385001/csv/veiculo_cor_iq3e7i.csv'
    # import_cor(filename_veiculo_cor)

    # filename_veiculo_modelo = f'{path}/v1588385550/csv/veiculo_modelo_ury3nj.csv'
    # import_modelo(filename_veiculo_modelo)

    # filename_veiculo_veiculo = 'https://res.cloudinary.com/sistema-int/raw/upload/v1588386054/csv/veiculo_veiculo_bjwhpq.csv'
    # import_veiculo(filename_veiculo_veiculo)

    # filename_pessoa_faccao = 'https://res.cloudinary.com/sistema-int/raw/upload/v1588391160/csv/pessoa_faccao_lb17pd.csv'
    # import_faccao(filename_pessoa_faccao)

    # filename_pessoa_pessoa = 'https://res.cloudinary.com/sistema-int/raw/upload/v1588386442/csv/pessoa_pessoa_ei4ado.csv'
    # import_pessoa(filename_pessoa_pessoa)

    # filename_pessoa_foto = 'https://res.cloudinary.com/sistema-int/raw/upload/v1588386919/csv/pessoa_foto_vakddv.csv'
    # import_foto(filename_pessoa_foto)

    toc = timeit.default_timer()
    return round(toc - tic, 2)


def create_data(filename, model):
    df = pd.read_csv(filename)
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
    for item in items[:1]:
        pprint(item)
        if item.get('address_number'):
            item['address_number'] = int(item.get('address_number'))
        else:
            item['address_number'] = None

        if item.get('cpf'):
            item['cpf'] = int(item.get('cpf'))
        else:
            item['cpf'] = None

        # if item.get('created_by_id'):
        #     item['created_by_id'] = int(item.get('created_by_id'))
        created_by_id = item.get('created_by_id')
        created_by = User.objects.get(pk=created_by_id)
        item['created_by'] = created_by

        # if item.get('faccao_id'):
        #     item['faccao_id'] = int(item.get('faccao_id'))
        faccao_id = item.get('faccao_id')
        faccao = Faccao.objects.get(pk=faccao_id)
        item['faccao'] = faccao

        obj = Pessoa(**item)
        data.append(obj)

    # data = [Pessoa(**item) for item in items]
    Pessoa.objects.bulk_create(data)


'''
User
'''


def import_user(filename):
    df = pd.read_csv(filename)
    aux = df.T.apply(dict).tolist()
    for item in aux:
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


def import_pessoa(filename):
    # 'slug',
    # 'nome',
    # 'sobrenome',
    # 'apelido',
    # 'mae',
    # 'pai',
    # 'faccao',
    # 'vitima',
    # 'created',
    # 'modified',
    # 'created_by',
    # 'address',
    # 'address_number',
    # 'complement',
    # 'district',
    # 'city',
    # 'uf',
    # 'cep',
    # 'country',
    # 'cpf',
    # 'rg',
    # 'cnh',
    create_pessoa(filename)


def import_foto(filename):
    create_data(filename, Foto)


def import_tatuagem():
    'slug',
    'pessoa',
    'foto',
    'descricao',
    'created',
    'modified',


def import_pessoacontato():
    'slug',
    'pessoa',
    'tipo',
    'telefone',
    'created',
    'modified',


def import_comparsa():
    'slug',
    'pessoa',
    'nome',
    'parente',
    'grau_parentesco',
    'observacao',
    'created',
    'modified',
    'cpf',
    'rg',
    'cnh',


def import_faccao(filename):
    create_data(filename, Faccao)


def import_pessoaveiculo():
    'slug',
    'pessoa',
    'veiculo',
    'created',
    'modified',
    'created_by',


'''
Ocorrencia
'''


def import_natureza():
    'slug',
    'artigo',
    'natureza',


def import_arma():
    'slug',
    'arma',


def import_infracao():
    'slug',
    'pessoa',
    'natureza',
    'qualificacao',
    'arma',
    'status',
    'created',
    'modified',
    'created_by',


def import_ocorrencia():
    'slug',
    'rai',
    'data_do_fato',
    'descricao',
    'created',
    'modified',
    'created_by',


def import_pessoaocorrencia():
    'slug',
    'pessoa',
    'ocorrencia',
    'created',
    'modified',
    'created_by',


def import_ocorrenciaveiculo():
    'slug',
    'ocorrencia',
    'veiculo',
    'created',
    'modified',
    'created_by',


def import_areaupm():
    'slug',
    'area_upm',


def import_motivacao():
    'slug',
    'titulo',

'''
Veiculo
'''


def import_veiculo(filename):
    create_data(filename, Veiculo)


def import_modelo(filename):
    create_data(filename, Modelo)


def import_cor(filename):
    create_data(filename, Cor)
