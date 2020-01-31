import names
import string
import timeit
from random import choice
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from core.models import
from core.management.commands.progress_bar import progressbar
from core.fix.data import


def gen_digits(max_length: int):
    '''Gera dígitos numéricos.'''
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_first_name():
    return names.get_first_name()


def gen_last_name():
    return names.get_last_name()


def gen_email(first_name: str, last_name: str, company: str = None):
    EMAIL = ('email', 'gmail', 'yahoo',)
    first_name = slugify(first_name)
    last_name = slugify(last_name)
    email = '{}.{}@{}.com'.format(first_name, last_name, sufix)
    return email
