class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def emitir_som(self) -> str:
        return ""
    
    def movimentar(self) -> str:
        return ""

if __name__ == "__main__":
    animal = Animal("Genérico", 5)
    print("Animal criado:", animal._nome)