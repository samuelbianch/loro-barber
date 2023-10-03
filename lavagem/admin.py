from django.contrib import admin
from lavagem import models

class Lavagem(admin.ModelAdmin):
    model = models.Lavagem
    
class Usuario(admin.ModelAdmin):
    model = models.Usuario

class Servico(admin.ModelAdmin):
    model = models.Servico

admin.site.register(models.Assinatura, Lavagem)
admin.site.register(models.Usuario, Usuario)
admin.site.register(models.Servico, Servico)
