def age_on_planets(idade_segundos):
    EARTH_ORBITAL_PERIOD = 31557600
    
    planet_ratios = {
        'Terra': 1.0,
        'Mercúrio': 0.2408467,
        'Vênus': 0.61519726,
        'Marte': 1.8808158,
        'Júpiter': 11.862615,
        'Saturno': 29.447498,
        'Urano': 84.016846,
        'Netuno': 164.79132
    }
    
    idades = {}
    for planeta, razao in planet_ratios.items():
        idades[planeta] = round(idade_segundos / (EARTH_ORBITAL_PERIOD * razao), 2)
    
    return idades

if __name__ == "__main__":
    print("Teste age_on_planets (1000000000):", age_on_planets(1000000000))