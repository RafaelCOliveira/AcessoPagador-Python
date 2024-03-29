from django.shortcuts import render, HttpResponse
from . import config, PagamentoCartao
import json, requests
from collections import namedtuple


# Create your views here.
def Pagamento(request):
    itens = []
    pagamento_Cartao = PagamentoCartao.PagamentoCartao()
 
    ListaPagamentos = pagamento_Cartao.Listar()
    
    for item in ListaPagamentos.Payments:
       infoPagamento = pagamento_Cartao.Consultar(item.PaymentId)
       itens.append(infoPagamento)

    return render(request, 'index.html',{'items':itens })

def Visualizar(request, id):
    pagamento_Cartao = PagamentoCartao.PagamentoCartao()
    item = pagamento_Cartao.Consultar(id)
    return render(request, 'visualizar.html',{'item':item })


def Capturar(request, id):
    pagamento_Cartao = PagamentoCartao.PagamentoCartao()
    item = pagamento_Cartao.Capturar(id)
    return render(request, 'visualizar.html',{'item':item })

def Cancelar(request, id):
    pagamento_Cartao = PagamentoCartao.PagamentoCartao()
    item = pagamento_Cartao.Cancelar(id)
    return render(request, 'visualizar.html',{'item':item })

def Pagar(request):
    return render(request, 'Pagar.html')

def RealizarPagamento(request):
    pagamento_Cartao = PagamentoCartao.PagamentoCartao()
    venda = pagamento_Cartao.RequestToVenda(request)
    item = pagamento_Cartao.Pagar(venda)
    return render(request, 'visualizar.html',{'item':item })


