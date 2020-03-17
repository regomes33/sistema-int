from django.db.models import Q


class SearchMixin(object):

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        search = self.request.GET.get('search')
        if search:
            return queryset.filter(
                Q(nome__icontains=search) |
                Q(sobrenome__icontains=search) |
                Q(apelido__icontains=search)
            )
        return queryset
