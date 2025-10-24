def raindrops(numero):
    resultado = ""
    
    if numero % 3 == 0:
        resultado += "Pling"
    if numero % 5 == 0:
        resultado += "Plang"
    if numero % 7 == 0:
        resultado += "Plong"
    
    if not resultado:
        return str(numero)
    
    return resultado

if __name__ == "__main__":
    print("Teste raindrops (15):", raindrops(15))
    print("Teste raindrops (35):", raindrops(35))
    print("Teste raindrops (105):", raindrops(105))
    print("Teste raindrops (8):", raindrops(8))