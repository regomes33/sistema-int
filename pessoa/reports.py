from django.shortcuts import render
from .models import Pessoa


def report_pessoas(request):
    pessoas = Pessoa.objects.all()
    context = {'object_list': pessoas}
    template_name = 'relatorios/report_pessoas.html'
    return render(request, template_name, context)
