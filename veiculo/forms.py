from django import forms

from .models import Modelo, Veiculo


class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = '__all__'


class ModeloForm(forms.ModelForm):

    class Meta:
        model = Modelo
        fields = '__all__'
