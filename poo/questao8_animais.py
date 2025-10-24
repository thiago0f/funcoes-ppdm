class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def emitir_som(self) -> str:
        return ""
    
    def movimentar(self) -> str:
        return ""

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self) -> str:
        return f"{self._nome} está latindo: Au Au!"
    
    def movimentar(self) -> str:
        return f"{self._nome} está correndo."

class Cavalo(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self) -> str:
        return f"{self._nome} está relinchando: Ih ih ih!"
    
    def movimentar(self) -> str:
        return f"{self._nome} está galopando."

class Preguica(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def emitir_som(self) -> str:
        return f"{self._nome} está fazendo barulho baixo: Zzz..."
    
    def movimentar(self) -> str:
        return f"{self._nome} está se movendo lentamente."

if __name__ == "__main__":
    cachorro = Cachorro("Rex", 5)
    cavalo = Cavalo("Spirit", 8)
    preguica = Preguica("Preguiça", 3)
    
    print(cachorro.emitir_som())
    print(cachorro.movimentar())
    print(cavalo.emitir_som())
    print(cavalo.movimentar())
    print(preguica.emitir_som())
    print(preguica.movimentar())