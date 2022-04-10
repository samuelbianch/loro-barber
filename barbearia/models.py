from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Barbeiro(models.Model):
    """Modelo de funcionario da barbearia"""
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField(datetime.now(), blank=True)
    foto = models.ImageField(upload_to='img/foto_barbeiro', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Barbeiro'
        verbose_name_plural = 'Barbeiros'
    
class Usuario(models.Model):
    """Modelo de usuário da barbearia"""
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField(datetime.now(), blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Servico(models.Model):
    """Modelo de serviço que será prestado pela barbearia"""
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = models.DurationField()
    image = models.ImageField(upload_to='img/imagem_servicos', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'