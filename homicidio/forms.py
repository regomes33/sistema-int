from django import forms

from .models import Homicidio


class HomicidioForm(forms.ModelForm):

    class Meta:
        model = Homicidio
        fields = (
            'rai',
            'data_do_homicidio',
            'forma',
            'area_upm',
            'vitima',
            'apelidovitima',
            'instrumento',
            'motivacao',
            'autoria',
            'nomeautor',
            'apelido',
            'genero',
            'district',
            'diligencia',
        )
