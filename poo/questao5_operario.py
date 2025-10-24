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

class Empregado(Pessoa):
    def __init__(self, nome="", endereco="", telefone="", codigo_setor=0, salario_base=0.0, imposto=0.0):
        super().__init__(nome, endereco, telefone)
        self.__codigo_setor = codigo_setor
        self.__salario_base = salario_base
        self.__imposto = imposto
    
    def get_codigo_setor(self):
        return self.__codigo_setor
    
    def get_salario_base(self):
        return self.__salario_base
    
    def get_imposto(self):
        return self.__imposto
    
    def set_codigo_setor(self, codigo_setor):
        self.__codigo_setor = codigo_setor
    
    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base
    
    def set_imposto(self, imposto):
        self.__imposto = imposto
    
    def calcular_salario(self):
        imposto_valor = self.__salario_base * (self.__imposto / 100)
        return self.__salario_base - imposto_valor

class Operario(Empregado):
    def __init__(self, nome="", endereco="", telefone="", codigo_setor=0, salario_base=0.0, imposto=0.0, 
                 valor_producao=0.0, comissao=0.0):
        super().__init__(nome, endereco, telefone, codigo_setor, salario_base, imposto)
        self.__valor_producao = valor_producao
        self.__comissao = comissao
    
    def get_valor_producao(self):
        return self.__valor_producao
    
    def get_comissao(self):
        return self.__comissao
    
    def set_valor_producao(self, valor_producao):
        self.__valor_producao = valor_producao
    
    def set_comissao(self, comissao):
        self.__comissao = comissao
    
    def calcular_salario(self):
        salario_base = super().calcular_salario()
        comissao_valor = self.__valor_producao * (self.__comissao / 100)
        return salario_base + comissao_valor

if __name__ == "__main__":
    operario = Operario("Operario 1", "Rua C", "456789123", 2, 2500, 8, 1000, 5)
    print("Salário do operário:", operario.calcular_salario())