from django import forms 
from .models import Produto, Marca, Usuario, Categoria


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['description', 'price', 'marca', 'categoria']

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome'] 

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'endereco']   

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']             