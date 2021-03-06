from django.shortcuts import render
from .models import Registro, Produto, Venda, ItemVenda

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def consulta_registro(request):
    registros = Registro.objects.all()
    context = {
        'registros': registros
    }
    return render(request, 'consulta_registro.html', context)

def registro_detalhado(request, pk):
    registro = Registro.objects.get(pk=pk)
    context = {
        'registro': registro
    }
    return render(request, 'detalhe_registro.html', context)
