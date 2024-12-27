import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the results from the CSV file
df = pd.read_csv("monkey_brainz.csv")
# Calculate n^4 and n^3 for the values in the DataFrame
df['n^4'] = df['N']**4
df['n^3'] = df['N']**3

n_values = np.arange(0, 10001)

# n4_values = n_values**4
n3_values = n_values**2

# Print the data to check it (optional)
print(df)
mana este teclado é impedido pelo meu fucking telemóvel a meter-se à frente do meu ecrã
e o copilot não me deixa ter uma ideia original
Like, não posso 

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot execution time vs N, M, L for each test
# We will assume that the relationship between execution time and the values is of interest.
# Adjust x and y as per what you want to visualize

# Plot Average Time vs N
plt.subplot(1, 1, 1)
plt.plot(df['N'], df['Average Time (s)'], label="Time vs N", marker='o')
plt.xlabel('L == M == N')
plt.ylabel('Average Time (s)')
plt.title('Tempos de execução experimentais vs Tempos de execução teóricos')

# Plot n^4 line for range 0 to 10000
# plt.plot(n_values, n4_values, label="L^2 * N^2 (0 to 10000)", linestyle='-', color='orange')

# Plot n^3 line for range 0 to 10000
plt.plot(n_values, n3_values, label="L^2 * N", linestyle='-', color='purple')
plt.grid(True)

# Show the plot
plt.legend()
plt.show()
