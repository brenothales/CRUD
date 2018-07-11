from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    Nome = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))

    nasc = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))

    idade = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))

    CPF = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))

    Tel = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'w3-input',
        }
    ))
    class Meta:
        model = Product
        fields = ['Nome', 'nasc', 'idade', 'CPF', 'email', 'Tel']