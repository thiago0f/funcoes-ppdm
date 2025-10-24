class Pessoa:
    def __init__(self, nome="", endereco="", telefone=""):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
    
    def get_nome(self):
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco
    
    def get_telefone(self):
        return self.__telefone
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_endereco(self, endereco):
        self.__endereco = endereco
    
    def set_telefone(self, telefone):
        self.__telefone = telefone

class Fornecedor(Pessoa):
    def __init__(self, nome="", endereco="", telefone="", valor_credito=0.0, valor_divida=0.0):
        super().__init__(nome, endereco, telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida
    
    def get_valor_credito(self):
        return self.__valor_credito
    
    def get_valor_divida(self):
        return self.__valor_divida
    
    def set_valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito
    
    def set_valor_divida(self, valor_divida):
        self.__valor_divida = valor_divida
    
    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida

if __name__ == "__main__":
    fornecedor = Fornecedor("Fornecedor 1", "Rua A", "123456789", 5000, 2000)
    print("Saldo do fornecedor:", fornecedor.obter_saldo())