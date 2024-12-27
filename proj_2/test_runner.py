import os
import subprocess
import time

# Path to the C++ executable
program_path = "./projeto"

# Directories for test inputs
test_dir = "tests"
time_log_file = "execution_times.csv"  # File to store timing results

# Initialize variables for calculating the average
total_time = 0
test_count = 0

# Open the timing log file for writing
with open(time_log_file, "w") as log:
    # Write the header for the CSV file
    log.write("TestFile,ExecutionTime(s)\n")

    # Process each test file in the test directory
    for test_file in sorted(os.listdir(test_dir)):
        test_path = os.path.join(test_dir, test_file)

        # Ensure it's a file
        if os.path.isfile(test_path):
            try:
                # Start the timer
                start_time = time.time()

                # Run the C++ program with the test file as input
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

                # Log the timing information
                log.write(f"{test_file},{execution_time:.6f}\n")

            except subprocess.CalledProcessError:
                continue

# Calculate and save the average execution time
average_time = total_time / test_count if test_count > 0 else 0
with open(time_log_file, "a") as log:
    log.write(f"\nAverageExecutionTime(s),{average_time:.6f}\n")
