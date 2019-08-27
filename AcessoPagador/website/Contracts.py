class CreditCard:
    '''
        CreditCard.CardNumber	Texto	16	Sim	Número do Cartão do comprador
        CreditCard.Holder	Texto	25	Sim	Nome do portador impresso no cartão
        CreditCard.ExpirationDate	Texto	7	Sim	Data de validade impresso no cartão
        CreditCard.SecurityCode	Texto	4	Sim	Código de segurança impresso no verso do cartão
        CreditCard.Brand	Texto	10	Sim	Bandeira do cartão
    '''
    def __init__(self, cardNumber, holder, expirationDate, securityCode, brand):
        self.CardNumber = cardNumber
        self.Holder = holder
        self.ExpirationDate = expirationDate
        self.SecurityCode = securityCode
        self.Brand = brand

class Customer:
    '''
        Customer.Name	Texto	255	Sim	Nome do comprador
    '''
    def __init__(self, name):
        self.Name = name


class Payment:
    '''
        Payment.Provider	Texto	15	Sim	Nome da provedora de Meio de Pagamento
        Payment.Type	Texto	100	Sim	Tipo do Meio de Pagamento
        Payment.Amount	Número	15	Sim	Valor do Pedido (ser enviado em centavos)
        Payment.Installments	Número	2	Sim	Número de Parcelas
    '''
    def __init__(self, provider, _type, amount, installments, creditCard):
        self.Provider = provider
        self.Type = _type
        self.Amount = amount
        self.Installments = installments
        self.CreditCard = creditCard

class Venda:
    def __init__(self, merchantOrderId, customer, payment):
        self.MerchantOrderId = merchantOrderId
        self.Customer = customer
        self.Payment = payment


