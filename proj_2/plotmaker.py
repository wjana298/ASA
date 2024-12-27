import csv
import matplotlib.pyplot as plt

# Load CSV data manually
data = []
with open("results.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({
            "V": int(row["V"]),
            "E": int(row["E"]),
            "L": int(row["L"]),
            "b": int(row["b"]),
            "seed": int(row["seed"]),
            "connectivity": float(row["connectivity"]),
            "runtime": float(row["runtime"])
        })

# Graph 1: Connectivity vs. Number of Vertices
plt.figure(figsize=(10, 6))
for b_value in [0, 1]:
    subset = [row for row in data if row["b"] == b_value]
    subset.sort(key=lambda x: x["V"])  # Sort by V for consistent plotting
    V = [row["V"] for row in subset]
    connectivity = [row["connectivity"] for row in subset]
    plt.plot(V, connectivity, marker='o', label=f"Connectivity (b={b_value})")

plt.xlabel("Number of Vertices (V)")
plt.ylabel("Connectivity Index")
plt.title("Connectivity vs. Number of Vertices")
plt.grid(True)
plt.legend()
plt.show()

# Graph 2: Runtime vs. Number of Vertices
plt.figure(figsize=(10, 6))
for L_value in set(row["L"] for row in data):
    subset = [row for row in data if row["L"] == L_value]
    subset.sort(key=lambda x: x["V"])
    V = [row["V"] for row in subset]
    runtime = [row["runtime"] for row in subset]
    plt.plot(V, runtime, marker='o', label=f"Runtime (L={L_value})")

plt.xlabel("Number of Vertices (V)")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime vs. Number of Vertices")
plt.grid(True)
plt.legend()
plt.show()

# Graph 3: Runtime vs. Theoretical Complexity
plt.figure(figsize=(10, 6))
data.sort(key=lambda x: x["V"])
V = [row["V"] for row in data]
runtime = [row["runtime"] for row in data]
theoretical_runtime = [v**2 for v in V]  # Example theoretical complexity (O(V^2))

plt.plot(V, runtime, marker='o', label="Measured Runtime")
plt.plot(V, theoretical_runtime, linestyle='--', label="Theoretical Runtime (O(V^2))")

plt.xlabel("Number of Vertices (V)")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime vs. Theoretical Complexity")
plt.grid(True)
plt.legend()
plt.show()
