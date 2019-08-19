from django import forms
from Apps.dataSet.models import DataSet


class AgregarDataSet(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = [
            'nombreDataSet',
            'tipoDataSet',
            'tamañoDataSet',
            'claseDataSet',
            'datos',
        ]
        labels = {
            'nombreDataSet': 'Nombre',
            'tipoDataSet': 'Tipo',
            'claseDataSet': 'Clase',
            'tamañoDataSet': 'Tamaño',
            'datos': 'Datos',
        }
        widgets = {
            'nombreDataSet': forms.TextInput(attrs={'class': 'form-control'}),
            'tipoDataSet': forms.Select(attrs={'class': 'form-control mdb-select colorful-select dropdown-ins'}),
            'claseDataSet': forms.TextInput(attrs={'class': 'form-control'}),
            # forms.TextInput(attrs={'class': 'form-control'}),
            'tamañoDataSet': forms.NumberInput(attrs={'class': 'form-control'}),
            'datos': forms.ClearableFileInput(attrs={'multiple': True}),

        }
