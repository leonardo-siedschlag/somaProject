from django.shortcuts import render

from django.shortcuts import render
from .models import Produto, Usuario
from .forms import ProductForm, MarcaForm, UsuarioForm, CategoriaForm
from django.shortcuts import redirect



def lista_produtos(request):
    produtos = Produto.objects.all
    return render(request, 'main_app/produtos.html',{'produtos':produtos})


def updateProdutoPage(request):
    produtos = Produto.objects.all
    return render(request, 'main_app/update_produtos.html',{'produtos':produtos})


def create_produto(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/produtos-form.html',{'form':form})


def update_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/produtos-form.html', {'form':form, 'produto': produto})

def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')

    return render(request, 'main_app/delete.html',{'produto': produto})


def create_marca(request):
    form = MarcaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/marca-form.html',{'form':form})

def create_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/usuario-form.html',{'form':form})

def delete_user(request, id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_produtos')

    return render(request, 'main_app/delete-user.html',{'usuario': usuario})

def dados_user(request):
    usuarios = Usuario.objects.all
    return render(request, 'main_app/dados-usuarios.html',{'usuarios':usuarios})



def updateUserPage(request):
    users = Usuario.objects.all
    return render(request, 'main_app/update-user.html',{'users':users})

def update_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/usuario-form.html', {'form':form, 'usuario': usuario})

def create_categoria(request):
    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'main_app/categoria-form.html',{'form':form})    


