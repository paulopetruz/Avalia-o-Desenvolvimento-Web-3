from django import forms
from core.models import FeriadoModel
from django.forms import ModelForm

class FeriadoForm(forms.Form):
    nome = forms.CharField(max_length=50)
    dia = forms.IntegerField()
    mes = forms.IntegerField()
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    
class FeriadoFormModel(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome','dia','mes']

    dados = {'nome':'Natal','dia':25,'mes':12}
    form = FeriadoModel(dados)
    form.is_valid()
    form.save()