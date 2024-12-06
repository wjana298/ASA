import matplotlib.pyplot as plt
import numpy as np
import time

def run_algorithm(n, m):
    # Simular a execução do algoritmo para dados de entrada n e m
    # Esta é uma versão simplificada para medir a complexidade

    # A complexidade de O(m^3 * n^2)
    result = (m ** 3) * (n ** 2)
    return result

# Definir os tamanhos de m e n para os testes
n_values = np.linspace(10, 100, 10, dtype=int)  # Tamanho da tabela de operações
m_values = np.linspace(10, 100, 10, dtype=int)  # Tamanho da sequência

# Medir o tempo de execução para diferentes valores de m e n
times_m = []
for m in m_values:
    start_time = time.time()
    run_algorithm(50, m)  # Fixamos n para 50 e variamos m
    times_m.append(time.time() - start_time)

times_n = []
for n in n_values:
    start_time = time.time()
    run_algorithm(n, 50)  # Fixamos m para 50 e variamos n
    times_n.append(time.time() - start_time)

# Plotar gráficos
plt.figure(figsize=(10, 5))

# Gráfico 1: Tempo de execução vs. Tamanho da sequência (m)
plt.subplot(1, 2, 1)
plt.plot(m_values, times_m, label="Tempo vs m", color="b", marker='o')
plt.xlabel("Tamanho da sequência (m)")
plt.ylabel("Tempo de execução (segundos)")
plt.title("Tempo de Execução vs Tamanho da Sequência")
plt.grid(True)

# Gráfico 2: Tempo de execução vs. Tamanho da tabela de operações (n)
plt.subplot(1, 2, 2)
plt.plot(n_values, times_n, label="Tempo vs n", color="r", marker='o')
plt.xlabel("Tamanho da tabela de operações (n)")
plt.ylabel("Tempo de execução (segundos)")
plt.title("Tempo de Execução vs Tamanho da Tabela de Operações")
plt.grid(True)

# Exibir os gráficos
plt.tight_layout()
plt.show()
