'''
Importa os dados do Cloudinary.
'''
import pandas as pd
import timeit
from django.contrib.auth.models import User, Group
from veiculo.models import Cor
from veiculo.models import Modelo
from veiculo.models import Veiculo


def my_import_data():
    tic = timeit.default_timer()

    path = 'https://res.cloudinary.com/sistema-int/raw/upload'

    # filename_veiculo_cor = f'{path}/v1588385001/csv/veiculo_cor_iq3e7i.csv'
    # import_cor(filename_veiculo_cor)

    # filename_veiculo_modelo = f'{path}/v1588385550/csv/veiculo_modelo_ury3nj.csv'
    # import_modelo(filename_veiculo_modelo)

    filename_veiculo_veiculo = f'https://res.cloudinary.com/sistema-int/raw/upload/v1588386054/csv/veiculo_veiculo_bjwhpq.csv'
    import_veiculo(filename_veiculo_veiculo)

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


def import_veiculo(filename):
    get_data(filename, Veiculo)


def import_modelo(filename):
    get_data(filename, Modelo)


def import_cor(filename):
    get_data(filename, Cor)


def get_data(filename, model):
    df = pd.read_csv(filename)
    aux = df.T.apply(dict).tolist()
    data = [model(**item) for item in aux]
    model.objects.bulk_create(data)
