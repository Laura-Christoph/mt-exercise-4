import re

# Step 1: Import necessary modules
path = '/Users/laurachristoph/Library/CloudStorage/OneDrive-UniversitätZürichUZH/CL/05_F24_MachineTranslation/mt-2024-exercise-4/ex04_code/models/deen_transformer_post/train.log'
# Step 5: Open input file
with open(path, "r") as file:
    # Step 6: Iterate over each line
    for line in file:
        # Step 7: Check if line matches conditions
        if re.search(r"Step:     \d+00\b", line) or "ppl" in line:
            # Step 8: Extract the relevant information
            match = re.search(r"(Step:     \d+00)|ppl: (\d+),", line)
            if match:
                if match.group(1):
                    print(match.group(1))
                elif match.group(2):
                    print("ppl:", match.group(2))
            # Step 8: Extract the relevant information
            match = re.search(r"(Step:     \d+00)|ppl: (\d+)", line)
            if match:
                if match.group(1):
                    print(match.group(1))
                elif match.group(2):
                    print("ppl:", match.group(2))
            # Step 8: Print the line
            print(line.strip())
            print(r'\n\n')
