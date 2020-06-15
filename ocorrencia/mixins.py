from django.db.models import Q



class SearchMixin(object):
    
    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        search = self.request.GET.get('search')
        filter_rai = self.request.GET.get('filter_rai')
        filter_data_do_homicidio = self.request.GET.get('filter_data_do_homicidio')
        filter_forma = self.request.GET.get('filter_forma')
        filter_area_upm = self.request.GET.get('filter_area_upm')
        filter_instrumento = self.request.GET.get('filter_instrumento')
        filter_motivacao = self.request.GET.get('filter_motivacao')
        filter_autoria = self.request.GET.get('filter_autoria')
        filter_genero = self.request.GET.get('filter_genero')
        filter_bairro = self.request.GET.get('filter_bairro')
        if search:
            queryset = queryset.filter(
                Q(rai__icontains=search) |
                Q(data_do_homicidio__icontains=search) |
                Q(forma__icontains=search) |
                Q(area_upm__icontains=search) |
                Q(instrumento__icontains=search) |
                Q(motivacao__icontains=search) |
                Q(autoria__icontains=search) |
                Q(genero__icontains=search) |
                Q(bairro__icontains=search)


            )

        if filter_rai:
            queryset = queryset.filter(Q(infracao__rai=filter_rai))

        if filter_data_do_homicidio:
            queryset = queryset.filter(Q(city=filter_data_do_homicidio))

        if filter_forma:
            queryset = queryset.filter(Q(faccao=filter_forma))

        if filter_area_upm:
            queryset = queryset.filter(Q(district=filter_area_upm))

        if filter_instrumento:
            queryset = queryset.filter(Q(district=filter_instrumento))

        if filter_motivacao:
            queryset = queryset.filter(Q(district=filter_motivacao))   

        if filter_autoria:
            queryset = queryset.filter(Q(district=filter_autoria))

        if filter_genero:
            queryset = queryset.filter(Q(district=filter_genero))

        if filter_bairro:
            queryset = queryset.filter(Q(district=filter_bairro))         

        return queryset