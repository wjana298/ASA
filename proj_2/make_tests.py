import subprocess
import os

# Path to the external program
program_path = "./p2_gerador"

# Range for N, M, and L (all equal)
values = range(50, 10001, 50)

# Directory to store the test files
output_dir = "tests"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop over the range to generate test files
for value in values:
    # Convert arguments to strings
    n = str(value)
    m = str(value)
    l = str(value)

    try:
        # Run the program with arguments
        result = subprocess.run(
            [program_path, n, m, l],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Capture the program's output
        output = result.stdout
        
        # Save the output to a file
        output_file = os.path.join(output_dir, f"test_{value}.txt")
        with open(output_file, "w") as file:
            file.write(output)

    except subprocess.CalledProcessError as e:
        print(f"Error running test with N=M=L={value}: {e.stderr}")
