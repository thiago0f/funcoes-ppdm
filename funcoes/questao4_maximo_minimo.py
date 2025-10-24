def maximo_minimo(lista):
    if not lista:
        return None, None
    return max(lista), min(lista)

if __name__ == "__main__":
    print("Teste maximo_minimo:", maximo_minimo([1, 5, 3, 9, 2]))