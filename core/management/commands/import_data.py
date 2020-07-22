from django.core.management.base import BaseCommand

from utils.import_data import my_import_data


class Command(BaseCommand):
    help = ''' Importa os dados. '''

    def handle(self, *args, **kwargs):
        print(my_import_data())
