import subprocess
import time

start_time = time.time()
print(start_time)
# Commands to run
prim_1 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_100_40.fasta", r"MSA\data\score_matrix.txt"]
prim_5 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_200_40.fasta", r"MSA\data\score_matrix.txt"]
prim_10 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_500_40.fasta", r"MSA\data\score_matrix.txt"]
prim_15 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_1000_40.fasta", r"MSA\data\score_matrix.txt"]
prim_20 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_1500_40.fasta", r"MSA\data\score_matrix.txt"]
prim_25 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_2000_40.fasta", r"MSA\data\score_matrix.txt"]
prim_30 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_2500_40.fasta", r"MSA\data\score_matrix.txt"]
prim_35 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_3500_40.fasta", r"MSA\data\score_matrix.txt"]
prim_40 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_5000_40.fasta", r"MSA\data\score_matrix.txt"]
prim_45 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_7500_40.fasta", r"MSA\data\score_matrix.txt"]
prim_50 = ["python", "aligment_to_msa.py", r"mutated_fox\test_long_aligment\mutated_foxp2_10000_40.fasta", r"MSA\data\score_matrix.txt"]



sp1 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_100_40.fasta", r"MSA\data\score_matrix.txt"]
sp5 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_200_40.fasta", r"MSA\data\score_matrix.txt"]
sp10 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_500_40.fasta", r"MSA\data\score_matrix.txt"]
sp15 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_1000_40.fasta", r"MSA\data\score_matrix.txt"]
sp20 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_1500_40.fasta", r"MSA\data\score_matrix.txt"]
sp25 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_2000_40.fasta", r"MSA\data\score_matrix.txt"]
sp30 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_2500_40.fasta", r"MSA\data\score_matrix.txt"]
sp35 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_3500_40.fasta", r"MSA\data\score_matrix.txt"]
sp40 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_5000_40.fasta", r"MSA\data\score_matrix.txt"]
sp45 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_7500_40.fasta", r"MSA\data\score_matrix.txt"]
sp50 = ["python", "SP_approxv5.py", r"mutated_fox\test_long_aligment\mutated_foxp2_10000_40.fasta", r"MSA\data\score_matrix.txt"]

# Define all command sequences in a list
# Define all command sequences in a list
commands = [
    # (prim_1, "prim_1"),
    # (prim_5, "prim_5"),
    # (prim_10, "prim_10"),
    # (prim_15, "prim_15"),
    # (prim_20, "prim_20"),
    # (prim_25, "prim_25"),
    # (prim_30, "prim_30"),
    # (prim_35, "prim_35"),
    # (prim_40, "prim_40"),
    # (prim_45, "prim_45"),
    # (prim_50, "prim_50")

    
    (sp1, "sp1"),
    (sp5, "sp5"),
    (sp10, "sp10"),
    (sp15, "sp15"),
    (sp20, "sp20"),
    (sp25, "sp25"),
    (sp30, "sp30"),
    (sp35, "sp35"),
    (sp40, "sp40"),
    (sp45, "sp45"),
    (sp50, "sp50")
    
]


# Store the output in a list
outputs = []

# Run each command 3 times
for cmd, label in commands:
    for i in range(3):
        result = subprocess.run(cmd, capture_output=True, text=True)
        full_output = result.stdout + result.stderr
        outputs.append(full_output)  # Capture full output
    print(f"{label} complete at {time.time() - start_time:.2f} seconds")

# Save all outputs to a file
with open("output_log.txt", "w") as f:
    for i, output in enumerate(outputs, 1):
        f.write(f"Run {i} Output:\n{output}\n")
        f.write("="*40 + "\n")  # Separator for readability

# Print total elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
