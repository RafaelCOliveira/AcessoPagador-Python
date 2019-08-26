import requests, json
from . import config
from collections import namedtuple

class PagamentoCartao:
    def __init__(self):
        self.BaseAddressConsulta = config.EndPoint["Consulta"]
        self.BaseAddressTransacional = config.EndPoint["Transacional"]
        self.headers = {'MerchantId': config.Merchant["MerchantId"], 'MerchantKey' : config.Merchant["MerchantKey"]}

    def Listar(self):
        url = self.BaseAddressConsulta + "v2/sales?merchantOrderId=" + config.MerchantOrderId
        retorno = requests.get(url, headers=self.headers)
        return self.ToObject(retorno.content)

    def Consultar(self, PaymentId):
         url = self.BaseAddressConsulta + "v2/sales/" + PaymentId
         retorno = requests.get(url, headers=self.headers)
         return json.loads(retorno.content)
    
    def Pagar(self, Venda):
        pass

    def Capturar(self, PaymentId):
        pass

    def Cancelar(self, PaymentId):
        pass

    def ToObject(self, obj):
        return json.loads(obj, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
