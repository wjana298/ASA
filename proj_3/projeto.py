"""
Resolução do projeto três de Análise e Síntese de Algoritmos

Autores: Miguel Trêpa, nº 109370 & Joana Guia, nº 99147
"""

import pulp
import sys

# Lê a primeira linha contendo o número de fábricas, países e crianças
factories, countries, children = map(int, sys.stdin.readline().strip().split())

# Lê as fábricas
factory_data = []
for _ in range(factories):
    factory_data.append(list(map(int, sys.stdin.readline().strip().split())))

# Lê os países
country_data = []
for _ in range(countries):
    country_data.append(list(map(int, sys.stdin.readline().strip().split())))

# Lê os pedidos das crianças
child_requests = []
for _ in range(children):
    child_requests.append(list(map(int, sys.stdin.readline().strip().split())))

# Debugging: Exibir as informações lidas
print("Factories:", factory_data)
print("Countries:", country_data)
print("Child Requests:", child_requests)
