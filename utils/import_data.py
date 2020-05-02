'''
Importa os dados do Cloudinary.
'''
import pandas as pd
import timeit
from django.contrib.auth.models import User, Group
from veiculo.models import Cor
from veiculo.models import Modelo


def my_import_data():
    tic = timeit.default_timer()

    path = 'https://res.cloudinary.com/sistema-int/raw/upload'

    # filename_veiculo_cor = path + 'veiculo_cor.csv'
    # filename_veiculo_cor = f'{path}/v1588385001/csv/veiculo_cor_iq3e7i.csv'
    # import_cor(filename_veiculo_cor)

    # filename_veiculo_modelo = f'{path}/v1588385550/csv/veiculo_modelo_ury3nj.csv'
    # import_modelo(filename_veiculo_modelo)

    toc = timeit.default_timer()
    return round(toc - tic, 2)


'''
Pessoa
'''


def import_pessoa():
    'slug',
    'nome',
    'sobrenome',
    'apelido',
    'mae',
    'pai',
    'faccao',
    'vitima',
    'created',
    'modified',
    'created_by',
    'address',
    'address_number',
    'complement',
    'district',
    'city',
    'uf',
    'cep',
    'country',
    'cpf',
    'rg',
    'cnh',


def import_foto():
    'slug',
    'pessoa',
    'foto',
    'created',
    'modified',


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


def import_faccao():
    'slug',
    'nome',
    'funcao',


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


def import_veiculo():
    'slug',
    'placa',
    'modelo',
    'cor',
    'observacao',
    'created',
    'modified',


def import_modelo(filename):
    df = pd.read_csv(filename)
    aux = df.T.apply(dict).tolist()
    data = [Modelo(**item) for item in aux]
    Modelo.objects.bulk_create(data)


def import_cor(filename):
    df = pd.read_csv(filename)
    aux = df.T.apply(dict).tolist()
    data = [Cor(**item) for item in aux]
    Cor.objects.bulk_create(data)
