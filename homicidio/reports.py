from datetime import datetime
from django.views.generic import ListView
from homicidio.mixins import SearchHomicidioMixin
from .models import Homicidio


class ReportHomicidioList(SearchHomicidioMixin, ListView):
    model = Homicidio
    template_name = 'reports/report_homicidio_list.html'

    def get_context_data(self, **kwargs):
        context = super(ReportHomicidioList, self).get_context_data(**kwargs)
        context['today'] = datetime.now().today()
        return context
