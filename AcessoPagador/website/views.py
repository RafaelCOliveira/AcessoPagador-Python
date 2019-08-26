from django.shortcuts import render, HttpResponse
from . import config, PagamentoCartao
import json, requests
from collections import namedtuple


# Create your views here.
def Pagamento(request):
    itens = []
    Pagamentos = PagamentoCartao.PagamentoCartao()
 
    ListaPagamentos = Pagamentos.Listar()
    
    for item in ListaPagamentos.Payments:
       ind = Pagamentos.Consultar(item.PaymentId)
       itens.append(ind)

    return render(request, 'index.html',{'items':itens })
