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

if __name__ == "__main__":
    pessoa = Pessoa("João", "Rua A", "123456789")
    print("Nome:", pessoa.get_nome())
    print("Endereço:", pessoa.get_endereco())
    print("Telefone:", pessoa.get_telefone())