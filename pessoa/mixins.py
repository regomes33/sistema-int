from django.db.models import Q


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
        search = self.request.GET.get('search')
        filter_natureza = self.request.GET.get('filter_natureza')
        filter_bairro = self.request.GET.get('filter_bairro')
        filter_cidade = self.request.GET.get('filter_cidade')
        filter_faccao = self.request.GET.get('filter_faccao')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(sobrenome__icontains=search) |
                Q(apelido__icontains=search)
            )

        if filter_natureza:
            queryset = queryset.filter(Q(infracao__natureza=filter_natureza))

        if filter_bairro:
            queryset = queryset.filter(Q(district=filter_bairro))

        if filter_cidade:
            queryset = queryset.filter(Q(city=filter_cidade))

        if filter_faccao:
            queryset = queryset.filter(Q(faccao=filter_faccao))

        return queryset
