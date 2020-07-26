from datetime import datetime

from django.views.generic import ListView

from homicidio.mixins import SearchHomicidioMixin

from .models import Homicidio


class ReportHomicidioList(SearchHomicidioMixin, ListView):
    model = Homicidio
    template_name = 'reports/report_homicidio_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReportHomicidioList, self).get_context_data(**kwargs)
        items_total = Homicidio.objects.values_list('id', flat=True).count()
        context['items_total'] = items_total
        context['today'] = datetime.now().today()
        return context
