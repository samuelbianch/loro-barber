from django.contrib import admin
from barbearia import models

class Barbeiro(admin.ModelAdmin):
    model = models.Barbeiro
    
class Usuario(admin.ModelAdmin):
    model = models.Usuario

class Servico(admin.ModelAdmin):
    model = models.Servico

admin.site.register(models.Barbeiro, Barbeiro)
admin.site.register(models.Usuario, Usuario)
admin.site.register(models.Servico, Servico)
