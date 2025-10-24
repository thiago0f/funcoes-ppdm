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

class Jaula:
    def __init__(self, animal):
        self._animal = animal
    
    def mostrar_animal(self):
        print(f"Na jaula tem um {self._animal.__class__.__name__}")
        print(self._animal.emitir_som())
        print(self._animal.movimentar())

if __name__ == "__main__":
    cachorro = Cachorro("Rex", 5)
    cavalo = Cavalo("Spirit", 8)
    preguica = Preguica("Preguiça", 3)
    
    jaula1 = Jaula(cachorro)
    jaula2 = Jaula(cavalo)
    jaula3 = Jaula(preguica)
    
    jaula1.mostrar_animal()
    print()
    jaula2.mostrar_animal()
    print()
    jaula3.mostrar_animal()