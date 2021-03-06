import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Registro(models.Model):
    date = models.DateField()



class Venda(models.Model):
    hora_da_venda = models.TimeField()
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)

class ItemVenda(models.Model):
    nome_item = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor_venda = models.FloatField()
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    imagem = models.FilePathField(path='/img')
