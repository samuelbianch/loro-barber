from django.shortcuts import render
from lavagem.models import Assinatura

def index(request):
    """Carrega a página principal da aplicação"""

    assinaturas = Assinatura.objects.order_by('-valor').filter(ativa=True)

    context = {
        "assinaturas": assinaturas
    }
    print(context)
    return render(request, 'index.html', context)