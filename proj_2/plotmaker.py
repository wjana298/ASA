import matplotlib.pyplot as plt
import numpy as np
import subprocess
import time
import random

# Simular diferentes complexidades teóricas
def O_linear(L, S):
    return L

def O_quadratic(L, S):
    return L**2

def O_cubic(L, S):
    return L**3

def O_mixed(L, S):
    return L**3 + L**2 * S

def O_increased(L, S):
    return L**3 * S + L**2

def O_interaction(L, S):
    return S * L

def O_linear_connections(L, C):
    return L * C

# Gerar entradas relevantes para o programa
def generate_relevant_input(stations, lines, connections):
    """
    Gera entradas relevantes para testar o algoritmo:
    - Cada estação tem pelo menos uma linha conectada.
    - Há redundâncias artificiais nas linhas.
    """
    input_data = f"{stations} {connections} {lines}\n"
    used_connections = set()

    # Gerar conexões básicas (cada estação com pelo menos uma linha)
    for line in range(lines):
        station_1 = random.randint(1, stations)
        station_2 = random.randint(1, stations)
        while station_1 == station_2:
            station_2 = random.randint(1, stations)
        input_data += f"{station_1} {station_2} {line + 1}\n"
        used_connections.add((station_1, station_2, line + 1))

    # Adicionar conexões extras para redundância
    extra_connections = connections - len(used_connections)
    while extra_connections > 0:
        station_1 = random.randint(1, stations)
        station_2 = random.randint(1, stations)
        line = random.randint(1, lines)
        if station_1 != station_2 and (station_1, station_2, line) not in used_connections:
            input_data += f"{station_1} {station_2} {line}\n"
            used_connections.add((station_1, station_2, line))
            extra_connections -= 1

    return input_data

# Executar o programa C++ e medir o tempo de execução
def run_cpp_program(stations, lines, connections):
    input_data = generate_relevant_input(stations, lines, connections)
    start_time = time.time()
    result = subprocess.run(['./projeto'], input=input_data, text=True, capture_output=True)
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Tempo em ms
    return elapsed_time

# Configuração dos valores de estações, linhas e conexões
stations_values = np.linspace(100, 1000, 100, dtype=int)  # Valores de estações (S)
lines_values = np.linspace(100, 1000, 100, dtype=int)  # Valores de linhas (L)
connections_per_station = 2  # Média de conexões por estação

# Calcular conexões totais com base no número de estações e linhas
connections_values = [stations * connections_per_station for stations in stations_values]

# Tempos experimentais e teóricos
experimental_times = []
theoretical_times_mixed = []
theoretical_times_linear = []
theoretical_times_quadratic = []
theoretical_times_interaction = []
# theoretical_times_increased = []

# Coletar dados para o gráfico
for stations, lines, connections in zip(stations_values, lines_values, connections_values):
    # Executar o programa 5 vezes e calcular a média
    elapsed_times = [run_cpp_program(stations, lines, connections) for _ in range(100)]
    avg_time = np.mean(elapsed_times)
    experimental_times.append(avg_time)

    # Calcular complexidades teóricas
    theoretical_times_mixed.append(O_mixed(lines, stations))
    theoretical_times_linear.append(O_linear(lines, stations))
    theoretical_times_quadratic.append(O_quadratic(lines, stations))
    theoretical_times_interaction.append(O_interaction(lines, stations))
    # theoretical_times_interaction.append(O_increased(lines, stations))

# Normalizar as complexidades teóricas para comparação
max_experimental = max(experimental_times)
theoretical_times_mixed = [t / max(theoretical_times_mixed) * max_experimental for t in theoretical_times_mixed]
theoretical_times_linear = [t / max(theoretical_times_linear) * max_experimental for t in theoretical_times_linear]
theoretical_times_quadratic = [t / max(theoretical_times_quadratic) * max_experimental for t in theoretical_times_quadratic]
theoretical_times_interaction = [t / max(theoretical_times_interaction) * max_experimental for t in theoretical_times_interaction]
# theoretical_times_increased = [t / max(theoretical_times_increased) * max_experimental for t in theoretical_times_increased]

# Plotar os gráficos
plt.figure(figsize=(12, 8))

# Gráfico de tempos experimentais
plt.plot(lines_values, experimental_times, label="Tempos Experimentais (C++)", marker='o', color="blue")

# Gráficos de complexidades teóricas
plt.plot(lines_values, theoretical_times_mixed, label="Complexidade O(L^3 + L^2 * S)", linestyle="--", color="red")
plt.plot(lines_values, theoretical_times_linear, label="Complexidade O(L)", linestyle="--", color="green")
plt.plot(lines_values, theoretical_times_quadratic, label="Complexidade O(L^2)", linestyle="--", color="orange")
plt.plot(lines_values, theoretical_times_interaction, label="Complexidade O(S * L)", linestyle="--", color="purple")
# plt.plot(lines_values, theoretical_times_increased, label = "Complexidade O(L^3 * S + L^2)", linestyle = "--", color = "yellow")

# Configurações do gráfico
plt.xlabel("Número de Linhas (L)", fontsize=12)
plt.ylabel("Tempo de Execução (ms)", fontsize=12)
plt.title("Comparação: Tempos Experimentais vs Complexidades Teóricas", fontsize=14)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
