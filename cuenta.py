class Cuenta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construyendo el objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extracto(self):
        print("Saldo: {} del titular {}".format(self.__saldo, self.__titular))
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def retirar(self, valor):
        self.__saldo -= valor
        #if(valor<= self.saldo):
         #   self.saldo -= valor
        #else:
         #   print("No cuenta con esa cantidad disponible para retirar")
            
    def transferir(self, valor, destino):
        self.retirar(valor)
        destino.depositar(valor)
        
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite