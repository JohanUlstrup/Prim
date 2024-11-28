import subprocess
import time

start_time = time.time()
print(start_time)
# Commands to run
prim_1 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_1.fasta", r"MSA\data\score_matrix.txt"]
prim_5 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_5.fasta", r"MSA\data\score_matrix.txt"]
prim_10 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_10.fasta", r"MSA\data\score_matrix.txt"]
prim_15 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_15.fasta", r"MSA\data\score_matrix.txt"]
prim_20 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_20.fasta", r"MSA\data\score_matrix.txt"]
prim_25 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_25.fasta", r"MSA\data\score_matrix.txt"]
prim_30 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_30.fasta", r"MSA\data\score_matrix.txt"]
prim_35 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_35.fasta", r"MSA\data\score_matrix.txt"]
prim_40 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_40.fasta", r"MSA\data\score_matrix.txt"]
prim_45 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_45.fasta", r"MSA\data\score_matrix.txt"]
prim_50 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_50.fasta", r"MSA\data\score_matrix.txt"]
prim_55 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_55.fasta", r"MSA\data\score_matrix.txt"]
prim_60 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_60.fasta", r"MSA\data\score_matrix.txt"]
prim_65 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_65.fasta", r"MSA\data\score_matrix.txt"]
prim_70 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_70.fasta", r"MSA\data\score_matrix.txt"]
prim_75 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_75.fasta", r"MSA\data\score_matrix.txt"]
prim_80 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_80.fasta", r"MSA\data\score_matrix.txt"]
prim_85 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_85.fasta", r"MSA\data\score_matrix.txt"]
prim_90 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_90.fasta", r"MSA\data\score_matrix.txt"]
prim_95 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_95.fasta", r"MSA\data\score_matrix.txt"]
prim_100 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_100.fasta", r"MSA\data\score_matrix.txt"]


sp1 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_1.fasta", r"MSA\data\score_matrix.txt"]
sp5 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_5.fasta", r"MSA\data\score_matrix.txt"]
sp10 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_10.fasta", r"MSA\data\score_matrix.txt"]
sp15 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_15.fasta", r"MSA\data\score_matrix.txt"]
sp20 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_20.fasta", r"MSA\data\score_matrix.txt"]
sp25 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_25.fasta", r"MSA\data\score_matrix.txt"]
sp30 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_30.fasta", r"MSA\data\score_matrix.txt"]
sp35 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_35.fasta", r"MSA\data\score_matrix.txt"]
sp40 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_40.fasta", r"MSA\data\score_matrix.txt"]
sp45 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_45.fasta", r"MSA\data\score_matrix.txt"]
sp50 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_50.fasta", r"MSA\data\score_matrix.txt"]
sp55 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_55.fasta", r"MSA\data\score_matrix.txt"]
sp60 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_60.fasta", r"MSA\data\score_matrix.txt"]
sp65 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_65.fasta", r"MSA\data\score_matrix.txt"]
sp70 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_70.fasta", r"MSA\data\score_matrix.txt"]
sp75 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_75.fasta", r"MSA\data\score_matrix.txt"]
sp80 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_80.fasta", r"MSA\data\score_matrix.txt"]
sp85 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_85.fasta", r"MSA\data\score_matrix.txt"]
sp90 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_90.fasta", r"MSA\data\score_matrix.txt"]
sp95 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_95.fasta", r"MSA\data\score_matrix.txt"]
sp100 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_100.fasta", r"MSA\data\score_matrix.txt"]

# Define all command sequences in a list
# Define all command sequences in a list
commands = [
    (prim_1, "prim_1"),
    (prim_5, "prim_5"),
    (prim_10, "prim_10"),
    (prim_15, "prim_15"),
    (prim_20, "prim_20"),
    (prim_25, "prim_25"),
    (prim_30, "prim_30"),
    (prim_35, "prim_35"),
    (prim_40, "prim_40"),
    (prim_45, "prim_45"),
    (prim_50, "prim_50"),
    (prim_55, "prim_55"),
    (prim_60, "prim_60"),
    (prim_65, "prim_65"),
    (prim_70, "prim_70"),
    (prim_75, "prim_75"),
    (prim_80, "prim_80"),
    (prim_85, "prim_85"),
    (prim_90, "prim_90"),
    (prim_95, "prim_95"),
    (prim_100, "prim_100"),
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
    (sp50, "sp50"),
    (sp55, "sp55"),
    (sp60, "sp60"),
    (sp65, "sp65"),
    (sp70, "sp70"),
    (sp75, "sp75"),
    (sp80, "sp80"),
    (sp85, "sp85"),
    (sp90, "sp90"),
    (sp95, "sp95"),
    (sp100, "sp100")
]


# Store the output in a list
outputs = []

# Run each command 3 times
for cmd, label in commands:
    for i in range(1):
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
