from __future__ import unicode_literals

from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome 

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100) 
    def __str__(self):
        return self.nome

class Marca(models.Model):
     id = models.AutoField(primary_key=True)
     nome = models.CharField(max_length=100)
     def __str__(self):
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca,  on_delete=models.CASCADE,)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    price =  models.DecimalField(max_digits=9, decimal_places=2)




def __str__(self):
    return self.description