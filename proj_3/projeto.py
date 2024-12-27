"""
Resolução do projeto três de Análise e Síntese de Algoritmos

Autores: Miguel Trêpa, nº 109370 & Joana Guia, nº 99147
"""

from pulp import *

factories = int(input())
countries = int(input())
children  = int(input())

print(factories, countries, children)

for i in range(factories):
    factory = input().split(" ")
    factory = [int(x) for x in factory]
    print(factory)