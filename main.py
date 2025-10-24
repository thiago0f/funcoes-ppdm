import sys
import os

# Adiciona os diretórios ao path para importar os módulos
sys.path.append(os.path.join(os.path.dirname(__file__), 'funcoes'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'poo'))

def main():
    print("=== Soluções de Atividades - Funções e POO em Python ===\n")
    
    # Importando e testando as funções
    print("1. Testando Funções:")
    
    from funcoes import questao1_soma
    from funcoes import questao2_media
    from funcoes import questao3_desconto
    from funcoes import questao4_maximo_minimo
    from funcoes import questao5_multiplicar
    from funcoes import questao6_raindrops
    from funcoes import questao7_age_on_planets
    from funcoes import questao8_calculate_energy_points
    
    print("- Soma de 5 e 3:", questao1_soma.soma(5, 3))
    print("- Média de 10 e 20:", questao2_media.media(10, 20))
    print("- Desconto de 100 com 15%:", questao3_desconto.desconto(100, 15))
    print("- Desconto de 100 com padrão:", questao3_desconto.desconto(100))
    print("- Máximo e mínimo de [1, 5, 3, 9, 2]:", questao4_maximo_minimo.maximo_minimo([1, 5, 3, 9, 2]))
    print("- Multiplicação de 4 e 5:", questao5_multiplicar.multiplicar(4, 5))
    print("- Raindrops de 15:", questao6_raindrops.raindrops(15))
    print("- Raindrops de 35:", questao6_raindrops.raindrops(35))
    print("- Raindrops de 105:", questao6_raindrops.raindrops(105))
    print("- Idade nos planetas (1000000000 segundos):")
    idades = questao7_age_on_planets.age_on_planets(1000000000)
    for planeta, idade in idades.items():
        print(f"  {planeta}: {idade} anos")
    print("- Pontos de energia (nível 20, itens [3, 5]):", questao8_calculate_energy_points.calculate_energy_points(20, [3, 5]))
    
    print("\n" + "="*50 + "\n")
    
    # Importando e testando as classes POO
    print("2. Testando POO:")
    
    from poo import questao2_fornecedor
    from poo import questao4_administrador
    from poo import questao5_operario
    from poo import questao6_vendedor
    from poo import questao9_examinar_animal
    from poo import questao10_jaulas
    
    # Teste das classes de pessoa e empregados
    print("Classes de Pessoas e Empregados:")
    fornecedor = questao2_fornecedor.Fornecedor("Fornecedor 1", "Rua A", "123456789", 5000, 2000)
    administrador = questao4_administrador.Administrador("Admin 1", "Rua B", "987654321", 1, 3000, 10, 500)
    operario = questao5_operario.Operario("Operario 1", "Rua C", "456789123", 2, 2500, 8, 1000, 5)
    vendedor = questao6_vendedor.Vendedor("Vendedor 1", "Rua D", "789123456", 3, 2000, 5, 5000, 3)
    
    print(f"- Saldo do fornecedor: {fornecedor.obter_saldo()}")
    print(f"- Salário do administrador: {administrador.calcular_salario()}")
    print(f"- Salário do operário: {operario.calcular_salario()}")
    print(f"- Salário do vendedor: {vendedor.calcular_salario()}")
    
    print("\nClasses de Animais:")
    cachorro = questao10_jaulas.Cachorro("Rex", 5)
    cavalo = questao10_jaulas.Cavalo("Spirit", 8)
    preguica = questao10_jaulas.Preguica("Preguiça", 3)
    
    # Examinando animais (polimorfismo)
    print("- Examinando animais:")
    questao9_examinar_animal.examinar_animal(cachorro)
    questao9_examinar_animal.examinar_animal(cavalo)
    questao9_examinar_animal.examinar_animal(preguica)
    
    print("\nJaulas do zoológico:")
    jaula1 = questao10_jaulas.Jaula(cachorro)
    jaula2 = questao10_jaulas.Jaula(cavalo)
    jaula3 = questao10_jaulas.Jaula(preguica)
    
    jaula1.mostrar_animal()
    print()
    jaula2.mostrar_animal()
    print()
    jaula3.mostrar_animal()

if __name__ == "__main__":
    main()