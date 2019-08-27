import requests, json
from . import config, Contracts
from collections import namedtuple

class PagamentoCartao:
    def __init__(self):
        self.BaseAddressConsulta = config.EndPoint["Consulta"]
        self.BaseAddressTransacional = config.EndPoint["Transacional"]
        self.headers = {'MerchantId': config.Merchant["MerchantId"], 'MerchantKey' : config.Merchant["MerchantKey"]}
        self.headersPost = {'MerchantId': config.Merchant['MerchantId'], 'MerchantKey' : config.Merchant['MerchantKey'], 'Content-Type':'application/json'}

    def Listar(self):
        url = self.BaseAddressConsulta + "v2/sales?merchantOrderId=" + config.MerchantOrderId
        retorno = requests.get(url, headers=self.headers)
        return self.ToObject(retorno.content)

    def Consultar(self, PaymentId):
         url = self.BaseAddressConsulta + "v2/sales/" + PaymentId
         retorno = requests.get(url, headers=self.headers)
         return json.loads(retorno.content)
    
    def Pagar(self, venda):
        url = self.BaseAddressTransacional + "v2/sales/"
        objseri = json.dumps(venda, default=lambda x: x.__dict__)        
        retorno = requests.post(url, headers = self.headersPost, data = objseri)
        Obj = self.ToObject(retorno.content)

        if retorno.status_code == 201:
            return self.Consultar(Obj.Payment.PaymentId)
        else:
            return None


    def Capturar(self, PaymentId):
        url = self.BaseAddressTransacional + "v2/sales/" + PaymentId + "/capture"
        retorno = requests.put(url, headers = self.headers)
        if retorno.status_code == 200:
            return self.Consultar(PaymentId)
        else:
            return None

    def Cancelar(self, PaymentId):
        url = self.BaseAddressTransacional + "v2/sales/" + PaymentId + "/void"
        retorno = requests.put(url, headers = self.headers)
        if retorno.status_code == 200:
            return self.Consultar(PaymentId)
        else:
            return None

    def ToObject(self, obj):
        return json.loads(obj, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    def RequestToVenda(self, _request):
        customer = Contracts.Customer(_request.POST.get("Name"))
        creditCard = Contracts.CreditCard(_request.POST.get("CardNumber"),_request.POST.get("Holder"),_request.POST.get("expirationDate"),_request.POST.get("SecurityCode"),_request.POST.get("Brand"))
        payment = Contracts.Payment(_request.POST.get("Provider"),_request.POST.get("Type"),_request.POST.get("Amount"),_request.POST.get("Installments"),creditCard)
        venda = Contracts.Venda(config.MerchantOrderId,customer,payment)
        return venda

