from dateutil.parser import parse
from django.db.models import Q


class SearchHomicidioMixin(object):

    def get_queryset(self):
        queryset = super(SearchHomicidioMixin, self).get_queryset()

        # Retorna somente as vítimas.
        queryset = queryset.filter(vitima__vitima=True)

        data = self.request.GET
        search = data.get('search')

        filter_forma = data.getlist('filter_forma')
        filter_area = data.getlist('filter_area')
        filter_motivacao = data.getlist('filter_motivacao')
        filter_genero = data.getlist('filter_genero')
        filter_bairro = data.getlist('filter_bairro')
        filter_cidade = data.getlist('filter_cidade')
        filter_data_inicial = data.get('filter_data_inicial')
        filter_data_final = data.get('filter_data_final')
        filter_autoria = data.getlist('filter_autoria')
        filter_ano = data.getlist('filter_ano')

        if filter_data_inicial:
            filter_data_inicial = parse(filter_data_inicial, dayfirst=True)

        if filter_data_final:
            filter_data_final = parse(filter_data_final, dayfirst=True)

        if search:
            queryset = queryset.filter(
                Q(forma__icontains=search) |
                Q(area_upm__area_upm__icontains=search) |
                Q(motivacao__titulo__icontains=search) |
                Q(vitima__nome__icontains=search) |
                Q(vitima__sobrenome__icontains=search) |
                Q(vitima__apelido__icontains=search) |
                Q(autoria__autoria__icontains=search)
            )

        if filter_forma:
            queryset = queryset.filter(Q(forma__in=filter_forma))

        if filter_area:
            queryset = queryset.filter(Q(area_upm__in=filter_area))

        if filter_motivacao:
            queryset = queryset.filter(Q(motivacao__in=filter_motivacao))

        if filter_genero:
            queryset = queryset.filter(Q(genero__in=filter_genero))

        if filter_bairro:
            queryset = queryset.filter(Q(district__in=filter_bairro))

        if filter_cidade:
            queryset = queryset.filter(Q(district__city__in=filter_cidade))

        if filter_ano:
            queryset = queryset.filter(
                Q(data_do_homicidio__year__in=filter_ano))

        if filter_data_inicial and filter_data_final:
            queryset = queryset.filter(
                data_do_homicidio__range=(
                    filter_data_inicial, filter_data_final)
            )

        if filter_autoria:
            queryset = queryset.filter(Q(autoria__in=filter_autoria))

        return queryset
