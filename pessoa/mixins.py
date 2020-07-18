from django.db.models import Q
from pprint import pprint


class PessoaSomenteMixin(object):
    '''
    Retorna somente pessoas, exceto vítimas.
    '''

    def get_queryset(self):
        queryset = super(PessoaSomenteMixin, self).get_queryset()
        queryset = queryset.filter(vitima=False)
        return queryset


class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()

        data = self.request.GET
        search = data.get('search')

        # Seleção múltipla
        # getlist é usado para pegar os vários itens do request.
        filter_status_atual = data.getlist('filter_status_atual')
        filter_natureza = data.getlist('filter_natureza')
        filter_bairro = data.getlist('filter_bairro')
        filter_cidade = data.getlist('filter_cidade')
        filter_faccao = data.getlist('filter_faccao')

        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(sobrenome__icontains=search) |
                Q(apelido__icontains=search)
            )

        if filter_status_atual:
            queryset = queryset.filter(Q(status_atual__in=filter_status_atual))

        if filter_natureza:
            queryset = queryset.filter(
                Q(infracao__natureza__in=filter_natureza)
            )
        if filter_bairro:
            queryset = queryset.filter(Q(district__in=filter_bairro))

        if filter_cidade:
            queryset = queryset.filter(Q(district__city__in=filter_cidade))

        if filter_faccao:
            queryset = queryset.filter(Q(faccao__in=filter_faccao))

        return queryset
