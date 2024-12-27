import os
import subprocess
import time
import openpyxl

# Path to the C++ binary
program_path = "./projeto"

# Directories for test inputs
test_dir = "tests"
excel_file = "execution_times.xlsx"  # File to save Excel data

# Initialize variables for calculating the average
total_time = 0
test_count = 0
results = []  # List to store test results

# Process each test file in the test directory
for test_file in sorted(os.listdir(test_dir)):
    test_path = os.path.join(test_dir, test_file)

    # Ensure it's a file
    if os.path.isfile(test_path):
        try:
            # Start the timer
            start_time = time.time()

            # Run the binary program with the test file as input
            subprocess.run(
                [program_path],
                input=open(test_path).read(),
                capture_output=True,
                text=True,
                check=True
            )

            # Stop the timer and calculate execution time
            end_time = time.time()
            execution_time = end_time - start_time

            # Update total time and test count
            total_time += execution_time
            test_count += 1

            # Append results to the list
            results.append((test_file, execution_time))

        except subprocess.CalledProcessError:
            continue

# Calculate the average execution time
average_time = total_time / test_count if test_count > 0 else 0

# Add the average time as the last entry
results.append(("AverageExecutionTime", average_time))

# Create and write to the Excel file
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Execution Times"

# Write headers
ws.append(["Test File", "Execution Time (s)"])

# Write results to Excel
for test_file, exec_time in results:
    ws.append([test_file, round(exec_time, 6)])

# Save the Excel file
wb.save(excel_file)
