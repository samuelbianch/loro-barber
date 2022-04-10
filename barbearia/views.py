from django.shortcuts import render


def index(request):
    """Carrega a página principal da aplicação"""
    return render(request, 'index.html')