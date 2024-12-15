import matplotlib.pyplot as plt
import numpy as np
import subprocess
import time

# Outras complexidades padrão para comparação
def O_1(m, n):
    return np.ones_like(m)  # Constante

def O_log_n(m, n):
    return np.log2(n + 1)  # Logarítmica em relação a n

def O_n(m, n):
    return n  # Linear em relação a n

def O_n2(m, n):
    return n**3  # Quadrática em relação a n

# Simular a complexidade teórica O(m^3 * n^2)
def theoretical_complexity(m, n):
    return m**3 * n**2

# Função para executar o programa C++ e medir o tempo de execução
def run_cpp_program(n, m, r):
    # Criar a entrada formatada para o programa
    input_data = f"{n} {m}\n"
    input_data += '\n'.join([' '.join(map(str, range(1, n+1))) for _ in range(n)]) + '\n'
    input_data += ' '.join(map(str, range(1, m+1))) + f"\n{r}\n"
    
    # Medir o tempo de execução
    start_time = time.time()
    result = subprocess.run(['./projeto'], input=input_data, text=True, capture_output=True)
    end_time = time.time()
    
    # Capturar o tempo total de execução em milissegundos
    elapsed_time = (end_time - start_time) * 1000  # Converter para ms
    return elapsed_time

# Configurar os valores de n e m
m_values = np.linspace(10, 500, 70, dtype=int)  # Valores de m
n_values = np.linspace(10, 500, 70, dtype=int)  # Valores de n
r = 100  # Valor esperado

# Obter os tempos experimentais do teu programa
experimental_times = []
for m, n in zip(m_values, n_values):
    elapsed_times = [run_cpp_program(n, m, r) for _ in range(20)]  # Executar 20 vezes
    avg_time = np.mean(elapsed_times)
    experimental_times.append(avg_time)

# Calcular os valores teóricos
theoretical_times = [theoretical_complexity(m, n) for m, n in zip(m_values, n_values)]

# Normalizar os valores teóricos para facilitar a comparação
max_experimental = max(experimental_times)
max_theoretical = max(theoretical_times)
theoretical_normalized = [t / max_theoretical * max_experimental for t in theoretical_times]
o_n2_normalized = [O_n2(m, n) / max_theoretical * max_experimental for m, n in zip(m_values, n_values)]

# Plotar os gráficos
plt.figure(figsize=(10, 6))

# Gráfico de tempos experimentais
plt.plot(m_values, experimental_times, label="Tempos Experimentais (C++)", marker='o', color="blue")

# Gráfico de complexidade teórica normalizada
plt.plot(m_values, theoretical_normalized, label="Complexidade Teórica O(m^3 * n^2)", linestyle="--", color="red")

# Gráfico de complexidade teórica O(n^2) normalizada
plt.plot(m_values, o_n2_normalized, label="Complexidade Teórica O(n^2)", linestyle="--", color="green")

# Configurações do gráfico
plt.xlabel("Tamanho da Entrada (m e n)", fontsize=12)
plt.ylabel("Tempo de Execução (ms)", fontsize=12)
plt.title("Comparação: Tempos Experimentais vs Complexidade Teórica", fontsize=14)
plt.legend()
plt.grid(True)

# Exibir o gráfico
plt.tight_layout()
plt.show()
