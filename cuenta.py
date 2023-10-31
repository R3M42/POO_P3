class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extracto(self):
        print("Saldo: {} del titular {}".format(self.saldo, self.titular))