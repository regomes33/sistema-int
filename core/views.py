from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def inicial(request):
    return render(request, 'index.html')
    data = {}
    data['user'] = request.user
    return render(request, 'index.html', data)


def registrarusuario(request):
    return render(request, 'registrar.html')
