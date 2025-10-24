def calculate_energy_points(nivel, itens_magicos):
    multiplos = set()
    
    for item in itens_magicos:
        multiplo = item
        while multiplo < nivel:
            multiplos.add(multiplo)
            multiplo += item
    
    return sum(multiplos)

if __name__ == "__main__":
    print("Teste calculate_energy_points:", calculate_energy_points(20, [3, 5]))