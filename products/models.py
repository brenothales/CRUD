from django.db import models


class Product(models.Model):
    Nome = models.CharField(max_length=45)
    nasc = models.DateField('Data de Nasc', null=True)
    idade = models.IntegerField('Idade', null=True)
    CPF = models.CharField(max_length=11, unique=True)
    email = models.EmailField('Email', unique=True, null=True)
    Tel = models.CharField('Telefone', max_length=9, null=True)
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Nome