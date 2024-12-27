import subprocess
import csv
import time

# Paths to the generator and main program
generator_path = "./p2_gerador"
program_path = "./projeto"

# Parameter ranges for test generation
V_range = range(10, 101, 10)  # Vertices (10 to 100 in steps of 10)
E_factor = 1.5                # Edges scale with vertices
L_range = range(2, 11, 2)     # Lines (2 to 10 in steps of 2)
b_values = [0, 1]             # Connectivity flag
seed_range = range(1, 6)      # Random seeds (1 to 5)

# Output CSV file
csv_file = "results.csv"

# Open CSV for writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["V", "E", "L", "b", "seed", "connectivity", "runtime"])
    writer.writeheader()

    test_count = 0
    for V in V_range:
        for L in L_range:
            E = int(V * E_factor)  # Scale edges with vertices
            for b in b_values:
                for seed in seed_range:
                    # Run the generator
                    generator_args = [generator_path, str(V), str(E), str(L), str(b), str(seed)]
                    generator_process = subprocess.run(generator_args, capture_output=True, text=True)
                    
                    if generator_process.returncode != 0:
                        print(f"Error running generator for V={V}, E={E}, L={L}, b={b}, seed={seed}")
                        continue
                    
                    # Pass generator output to the main program
                    program_start = time.time()
                    program_process = subprocess.run(
                        [program_path],
                        input=generator_process.stdout,
                        capture_output=True,
                        text=True
                    )
                    program_end = time.time()

                    if program_process.returncode != 0:
                        print(f"Error running program for V={V}, E={E}, L={L}, b={b}, seed={seed}")
                        continue

                    # Collect and write results to CSV
                    connectivity = program_process.stdout.strip()
                    runtime = program_end - program_start
                    writer.writerow({
                        "V": V,
                        "E": E,
                        "L": L,
                        "b": b,
                        "seed": seed,
                        "connectivity": connectivity,
                        "runtime": runtime
                    })
                    test_count += 1
                    print(f"Test case {test_count}: V={V}, E={E}, L={L}, b={b}, seed={seed} - Done")

print(f"All test cases complete. Results saved to {csv_file}.")
