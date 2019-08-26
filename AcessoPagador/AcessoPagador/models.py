from django.db import models

class CreditCard:
    def __init__(self):
        self.CardNumber = ""
        self.Holder = ""
        self.ExpirationDate = ""
        self.SecurityCode = ""
        self.Brand = "" 

class Customer:
    def __init__(self):
        self.Name = ""

class Link:
    def __init__(self):
        self.Method = ""
        self.Rel = ""
        self.Href = ""

class Payment:
    def __init__(self):
        self.Provider = "" 
        self.Type = "" 
        self.Amount = 0.0
        self.Installments = 0
        self.creditCard = CreditCard()
        self.ProofOfSale = ""
        self.AcquirerTransactionId = "" 
        self.AuthorizationCode = "" 
        self.PaymentId = "" 
        self.ReceivedDate = ""
        self.ReasonCode = "" 
        self.ReasonMessage = "" 
        self.Status = "" 
        self.MsgStatus = "" 
        self.ProviderReturnCode = "" 
        self.ProviderReturnMessage = "" 
        self.Links = Link()
        self.Payments = "" 

class Venda:
    def __init__(self):
        self.MerchantOrderId = ""
        self.Customer = Customer()
        self.Payment = Payment()
    


