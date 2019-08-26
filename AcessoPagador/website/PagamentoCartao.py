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
        url = self.BaseAddressTransacional + "v2/sales/"        
        retorno = requests.post(url, headers = self.headers, data = Venda)

        if retorno.status_code == 200:
            return json.loads(retorno.content.decode('utf-8'))
        else:
            return None


    def Capturar(self, PaymentId):
        url = self.BaseAddressTransacional + "v2/sales/" + PaymentId + "/capture"
        retorno = requests.put(url, headers = self.headers)
        if retorno.status_code == 200:
            return True
        else:
            return False

    def Cancelar(self, PaymentId):
        url = self.BaseAddressTransacional + "v2/sales/" + PaymentId + "/void"
        retorno = requests.put(url, headers = self.headers)
        if retorno.status_code == 200:
            return True
        else:
            return False

    def ToObject(self, obj):
        return json.loads(obj, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
