from django.test import TestCase
from usuarios.models import cadastroUsuario
# Create your tests here.
class cadastroUsuarioTestCase(TestCase):
    def test_add(self):
        cadastroUsuario.objects.create(nome='Arthur',
                                       rgfuncional='12345')
        cadastroUsuario.objects.create(nome='Renato',
                                       rgfuncional='12345')
    
    def test_list(self):
        list = cadastroUsuario.objects.all()
        
        for item in list:
            print(item)