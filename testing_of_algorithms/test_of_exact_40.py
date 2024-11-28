import subprocess
import time

start_time = time.time()

exact10 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_10_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact20 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_20_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact30 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_30_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact40 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_40_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact50 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_50_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact60 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_60_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact70 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_70_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact80 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_80_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact90 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_90_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact100 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_100_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact120 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_120_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact140 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_140_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact160 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_160_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact180 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_180_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]
exact200 = ["python", "sp_exact_3.py", r"mutated_fox\exact_40\mutated_foxp2_200_40.fasta", "-g", "5", "-m", r"MSA\data\score_matrix.txt"]

prim10 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_10_40.fasta",  r"MSA\data\score_matrix.txt"]
prim20 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_20_40.fasta",  r"MSA\data\score_matrix.txt"]
prim30 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_30_40.fasta",  r"MSA\data\score_matrix.txt"]
prim40 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_40_40.fasta", r"MSA\data\score_matrix.txt"]
prim50 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_50_40.fasta",  r"MSA\data\score_matrix.txt"]
prim60 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_60_40.fasta",  r"MSA\data\score_matrix.txt"]
prim70 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_70_40.fasta",  r"MSA\data\score_matrix.txt"]
prim80 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_80_40.fasta",  r"MSA\data\score_matrix.txt"]
prim90 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_90_40.fasta",  r"MSA\data\score_matrix.txt"]
prim100 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_100_40.fasta",  r"MSA\data\score_matrix.txt"]
prim120 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_120_40.fasta",  r"MSA\data\score_matrix.txt"]
prim140 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_140_40.fasta",  r"MSA\data\score_matrix.txt"]
prim160 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_160_40.fasta",  r"MSA\data\score_matrix.txt"]
prim180 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_180_40.fasta",  r"MSA\data\score_matrix.txt"]
prim200 = ["python", "aligment_to_msa.py", r"mutated_fox\exact_40\mutated_foxp2_200_40.fasta",  r"MSA\data\score_matrix.txt"]

sp10 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_10_40.fasta",  r"MSA\data\score_matrix.txt"]
sp20 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_20_40.fasta",  r"MSA\data\score_matrix.txt"]
sp30 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_30_40.fasta",  r"MSA\data\score_matrix.txt"]
sp40 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_40_40.fasta",  r"MSA\data\score_matrix.txt"]
sp50 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_50_40.fasta",  r"MSA\data\score_matrix.txt"]
sp60 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_60_40.fasta",  r"MSA\data\score_matrix.txt"]
sp70 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_70_40.fasta",  r"MSA\data\score_matrix.txt"]
sp80 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_80_40.fasta",  r"MSA\data\score_matrix.txt"]
sp90 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_90_40.fasta",  r"MSA\data\score_matrix.txt"]
sp100 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_100_40.fasta",  r"MSA\data\score_matrix.txt"]
sp120 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_120_40.fasta",  r"MSA\data\score_matrix.txt"]
sp140 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_140_40.fasta",  r"MSA\data\score_matrix.txt"]
sp160 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_160_40.fasta",  r"MSA\data\score_matrix.txt"]
sp180 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_180_40.fasta",  r"MSA\data\score_matrix.txt"]
sp200 = ["python", "SP_approxv5.py", r"mutated_fox\exact_40\mutated_foxp2_200_40.fasta",  r"MSA\data\score_matrix.txt"]


# Commands to run


# Define all command sequences in a list
# Define all command sequences in a list
commands = [
    (exact10, "exact10"),
    (exact20, "exact20"),
    (exact30, "exact30"),
    (exact40, "exact40"),
    (exact50, "exact50"),
    (exact60, "exact60"),
    (exact70, "exact70"),
    (exact80, "exact80"),
    (exact90, "exact90"),
    (exact100, "exact100"),
    (exact120, "exact120"),
    (exact140, "exact140"),
    (exact160, "exact160"),
    (exact180, "exact180"),
    (exact200, "exact200"),
    
    (prim10, "prim10"),
    (prim20, "prim20"),
    (prim30, "prim30"),
    (prim40, "prim40"),
    (prim50, "prim50"),
    (prim60, "prim60"),
    (prim70, "prim70"),
    (prim80, "prim80"),
    (prim90, "prim90"),
    (prim100, "prim100"),
    (prim120, "prim120"),
    (prim140, "prim140"),
    (prim160, "prim160"),
    (prim180, "prim180"),
    (prim200, "prim200"),
    
    (sp10, "sp10"),
    (sp20, "sp20"),
    (sp30, "sp30"),
    (sp40, "sp40"),
    (sp50, "sp50"),
    (sp60, "sp60"),
    (sp70, "sp70"),
    (sp80, "sp80"),
    (sp90, "sp90"),
    (sp100, "sp100"),
    (sp120, "sp120"),
    (sp140, "sp140"),
    (sp160, "sp160"),
    (sp180, "sp180"),
    (sp200, "sp200")
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
with open("output_log_exact.txt", "w") as f:
    for i, output in enumerate(outputs, 1):
        f.write(f"Run {i} Output:\n{output}\n")
        f.write("="*40 + "\n")  # Separator for readability

# Print total elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
