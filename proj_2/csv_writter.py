import os
import subprocess
import time
import csv

# Constants for configurable values
AVERAGE = 100  # Number of times to repeat each test for averaging

# Path to the binary program
program_path = "./projeto"

# Directories and output file
test_dir = "tests"
output_csv = "monkey_brainz.csv"

# Function to read N, M, and L from the test file
def read_test_params(test_path):
    with open(test_path, "r") as file:
        first_line = file.readline().strip()
        N, M, L = map(int, first_line.split())
        return N, M, L

# Collect all test files and their parameters
test_files = []
for test_file in os.listdir(test_dir):
    test_path = os.path.join(test_dir, test_file)
    if os.path.isfile(test_path):  # Ensure it's a file
        try:
            # Read parameters from the file
            N, M, L = read_test_params(test_path)
            test_files.append((test_file, N, M, L, test_path))
        except Exception:
            continue

# Sort the test files by N, M, and L
test_files.sort(key=lambda x: (x[1], x[2], x[3]))  # Sort by N, then M, then L

# Open the CSV file for writing
with open(output_csv, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write the CSV header
    writer.writerow(["Test File", "N", "M", "L", "Average Time (s)"])

    # Process each test file in order
    for test_file, N, M, L, test_path in test_files:
        # try:
            # Measure execution time over AVERAGE runs
            
            total_time = 0
            for _ in range(AVERAGE):
                start_time = time.time()
                subprocess.run(
                    [program_path],
                    input=open(test_path).read(),
                    capture_output=True,
                    text=True,
                    check=True
                )
                end_time = time.time()
                if (end_time == -1 or start_time == -1):
                    continue
                total_time += end_time - start_time
                if (total_time < 0):
                    total_time -= end_time - start_time
                    break

            # Calculate the average time
            avg_time = total_time / AVERAGE

            # Write the result to the CSV
            writer.writerow([test_file, N, M, L, round(avg_time, 6)])

        # except subprocess.CalledProcessError:
            # continue
