import subprocess
import time
start_time = time.time()
# The command you want to run
prim_1 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_1.fasta", r"MSA\data\score_matrix.txt"]
prim_10 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_10.fasta", r"MSA\data\score_matrix.txt"]
prim_50 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_50.fasta", r"MSA\data\score_matrix.txt"]
prim_100 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_100.fasta", r"MSA\data\score_matrix.txt"]
prim_150 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_150.fasta", r"MSA\data\score_matrix.txt"]
prim_200 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_200.fasta", r"MSA\data\score_matrix.txt"]
prim_300 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_300.fasta", r"MSA\data\score_matrix.txt"]
prim_400 = ["python", "aligment_to_msa.py", r"mutated_fox\mutated_foxp2_1000_400.fasta", r"MSA\data\score_matrix.txt"]

sp_1 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_1.fasta", r"MSA\data\score_matrix.txt"]
sp_10 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_10.fasta", r"MSA\data\score_matrix.txt"]
sp_50 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_50.fasta", r"MSA\data\score_matrix.txt"]
sp_100 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_100.fasta", r"MSA\data\score_matrix.txt"]
sp_150 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_150.fasta", r"MSA\data\score_matrix.txt"]
sp_200 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_200.fasta", r"MSA\data\score_matrix.txt"]
sp_300 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_300.fasta", r"MSA\data\score_matrix.txt"]
sp_400 = ["python", "SP_approxv5.py", r"mutated_fox\mutated_foxp2_1000_400.fasta", r"MSA\data\score_matrix.txt"]



# Store the output in a list
outputs = []

# Run the command 3 times
for i in range(3):
    result = subprocess.run(prim_1, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_1 complet",time.time())


# Run the command 3 times
for i in range(3):
    result = subprocess.run(prim_10, capture_output=True, text=True)
    full_output = result.stdout + re.stderr
    outputs.append(full_output)  # Capture full output

print("prim_10 complet",time.time())



# Run the command 3 times
for i in range(3):
    result = subprocess.run(prim_50, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_50 complet",time.time())

# Run the command 3 times
for i in range(3):
    result = subprocess.run(prim_100, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_100 complet",time.time())

for i in range(3):
    result = subprocess.run(prim_150, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_150 complet",time.time())


for i in range(3):
    result = subprocess.run(prim_200, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_200 complet",time.time())


for i in range(3):
    result = subprocess.run(prim_300, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_300 complet",time.time())


for i in range(3):
    result = subprocess.run(prim_400, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("prim_400 complet",time.time())

##SP approx
# Run the command 3 times
for i in range(3):
    result = subprocess.run(sp_1, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_1 complet",time.time())


# Run the command 3 times
for i in range(3):
    result = subprocess.run(sp_10, capture_output=True, text=True)
    full_output = result.stdout + re.stderr
    outputs.append(full_output)  # Capture full output

print("sp_10 complet",time.time())



# Run the command 3 times
for i in range(3):
    result = subprocess.run(sp_50, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output


print("sp_50 complet",time.time())

# Run the command 3 times
for i in range(3):
    result = subprocess.run(sp_100, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_100 complet",time.time())

#sp 2500
for i in range(3):
    result = subprocess.run(sp_150, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_150 complet",time.time())

#sp5000
for i in range(3):
    result = subprocess.run(sp_200, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_200 complet",time.time())

#SP 7500
for i in range(3):
    result = subprocess.run(sp_300, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_300 complet",time.time())

for i in range(3):
    result = subprocess.run(sp_400, capture_output=True, text=True)
    full_output = result.stdout + result.stderr
    outputs.append(full_output)  # Capture full output

print("sp_400 complet",time.time())






# Save all outputs to a file
with open("output_log.txt", "w") as f:
    for i, output in enumerate(outputs, 1):
        f.write(f"Run {i} Output:\n{output}\n")
        f.write("="*40 + "\n")  # Separator for readability

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")