from django.db.models import Q


class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        search = self.request.GET.get('search')

        filter_forma = self.request.GET.get('filter_forma')
        filter_area_upm = self.request.GET.get('filter_area_upm')
        filter_motivacao = self.request.GET.get('filter_motivacao')
        filter_bairro = self.request.GET.get('filter_bairro')

        if search:
            queryset = queryset.filter(
                Q(forma__icontains=search) |
                Q(area_upm__icontains=search) |
                Q(motivacao__icontains=search)
            )

        if filter_forma:
            queryset = queryset.filter(Q(forma=filter_forma))

        if filter_area_upm:
            queryset = queryset.filter(Q(homicidio__area_upm=filter_area_upm))

        if filter_motivacao:
            queryset = queryset.filter(Q(motivacao=filter_motivacao))

        if filter_bairro:
            queryset = queryset.filter(Q(district=filter_bairro))

        return queryset
