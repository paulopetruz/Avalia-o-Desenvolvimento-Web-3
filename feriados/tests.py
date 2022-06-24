from django.test import TestCase
from Feriado.forms import FeriadoForm

class feriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'feriado')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'Feriado.html')

class FeriadoFormTest(TestCase):
    def test_form_has_fields(self):
        form = FeriadoForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome='dia de são nunca')
        self.assertEqual('DIA DE SÃO NUNCA', form.cleaned_data['nome'])

    def test_must_be_capitalized(self):
        form = self.make_validated_form()
        self.assertEqual('TIRADENTES', form.cleaned_data['nome'])
        
    def make_validated_form(self, **kwargs):
        valid = dict(
            nome='Tiradentes',
            dia=14,
            mes=4
        )
        data = dict(valid, **kwargs)
        form = FeriadoForm(data)
        form.is_valid()
        return form