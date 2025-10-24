def desconto(valor, percentual=10):
    return valor - (valor * percentual / 100)

if __name__ == "__main__":
    print("Teste desconto:", desconto(100, 15))
    print("Teste desconto padrão:", desconto(100))