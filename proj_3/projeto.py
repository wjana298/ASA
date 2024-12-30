"""
Resolução do projeto três de Análise e Síntese de Algoritmos

Autores: Miguel Trêpa, nº 109370 & Joana Guia, nº 99147
"""

import pulp
import sys

# Coleção de dados
# Este passo tem complexidade O(n + m + c), onde 
# n é o número de fábricas, m é o número de países e c é o número de crianças

# factories, countries, children = [int(n) for n in input().split(" ")]

# print(factories, countries, children)

for line in sys.stdin:
    print(line.strip())

# print(f"Factories: {factories}")
# for i in range(factories):
#     factory = input().split(" ")
#     factory = [int(x) for x in factory]
#     print(factory)

# print(f"Countries: {countries}")
# for i in range(countries):
#     country = input().split(" ")
#     country = [int(x) for x in country]
#     print(country)

# print(f"Children: {children}")
# for i in range(children):
#     child = input().split(" ")
#     child = [int(x) for x in child]
#     print(child)