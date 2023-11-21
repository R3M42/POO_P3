class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extracto(self):
        print("Saldo: {} del titular {}".format(self.saldo, self.titular))
        
    def depositar(self, valor):
        self.saldo += valor
        
    def retirar(self, valor):
        if(valor<= self.saldo):
            self.saldo -= valor
        else:
            print("No cuenta con esa cantidad disponible para retirar")