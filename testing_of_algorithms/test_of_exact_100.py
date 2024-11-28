# import glob
# import subprocess
# import time
# import re
# import statistics

# # Start time for total elapsed time tracking
# start_time = time.time()

# # Directory containing files
# directory_path = "mutated_fox\\exact_100\\*.fasta"

# # Retrieve all .fasta files in the directory and sort them by the number in the filename
# file_list = glob.glob(directory_path)

# # Regular expression to extract the number part of each filename (e.g., `100` in `mutated_foxp2_100_3_100.fasta`)
# number_pattern = re.compile(r"mutated_foxp2_(\d+)_")

# # Sort the file list by the extracted numeric value
# file_list.sort(key=lambda x: int(number_pattern.search(x).group(1)))

# # Store the output in a list for logging purposes
# outputs = []

# # Lists to store mean scores and times for each command
# excat_scores, excat_times = [], []
# prim10_scores, prim10_times = [], []
# sp10_scores, sp10_times = [], []

# # Define command templates with placeholders for the file paths
# commands = {
#     "excat": ["python", "sp_exact_3.py", "{file_path}", "-g", "5", "-m", r"MSA\data\score_matrix.txt"],
#     "prim10": ["python", "aligment_to_msa.py", "{file_path}", r"MSA\data\score_matrix.txt"],
#     "sp10": ["python", "SP_approxv5.py", "{file_path}", r"MSA\data\score_matrix.txt"]
# }

# # Regular expression to match the score and time in each output
# score_pattern = re.compile(r"(\d+)\n([\d.]+)")

# # Run each command for each file in the sorted folder list, 3 times each
# for file_path in file_list:
#     for label, cmd_template in commands.items():
#         scores, times = [], []
        
#         for _ in range(3):  # Run each command 3 times
#             # Substitute the file path into the command template
#             cmd = [part.replace("{file_path}", file_path) for part in cmd_template]
            
#             # Run the command and capture output
#             result = subprocess.run(cmd, capture_output=True, text=True)
#             full_output = result.stdout + result.stderr
#             outputs.append(f"{label} - {file_path}:\n{full_output}")  # Capture full output for logging
            
#             # Parse the score and time from the output
#             match = score_pattern.search(full_output)
#             if match:
#                 score = int(match.group(1))
#                 time_taken = float(match.group(2))
#                 scores.append(score)
#                 times.append(time_taken)
        
#         # Calculate the mean of scores and times for the 3 runs
#         if scores and times:
#             mean_score = statistics.mean(scores)
#             mean_time = statistics.mean(times)
            
#             # Store the mean values in the appropriate lists based on the label
#             if label == "excat":
#                 excat_scores.append(mean_score)
#                 excat_times.append(mean_time)
#             elif label == "prim10":
#                 prim10_scores.append(mean_score)
#                 prim10_times.append(mean_time)
#             elif label == "sp10":
#                 sp10_scores.append(mean_score)
#                 sp10_times.append(mean_time)
        
#         # Print progress
#         print(f"{label} for {file_path} (mean of 3 runs) complete at {time.time() - start_time:.2f} seconds")

# # Save all outputs to a file for full logging
# with open("output_log_exact_100.txt", "w") as f:
#     for output in outputs:
#         f.write(output + "\n")
#         f.write("="*40 + "\n")  # Separator for readability

# # Print final mean scores and times for each command
# print("list:",file_list)
# print("excat scores (mean):", excat_scores)
# print("excat times (mean):", excat_times)
# print("prim10 scores (mean):", prim10_scores)
# print("prim10 times (mean):", prim10_times)
# print("sp10 scores (mean):", sp10_scores)
# print("sp10 times (mean):", sp10_times)

# # Print total elapsed time
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.6f} seconds")





import glob
import subprocess
import time
import re
import statistics

# Start time for total elapsed time tracking
start_time = time.time()

# Directory containing files
directory_path = "mutated_fox\\mutation\\*.fasta"

# Retrieve all .fasta files in the directory and sort them by the number in the filename
file_list = glob.glob(directory_path)

# Regular expression to extract the number part of each filename (e.g., `100` in `mutated_foxp2_1000_3_100.fasta`)
number_pattern = re.compile(r"mutated_foxp2_\d+_3_(\d+)")

# Sort the file list by the extracted numeric value
file_list.sort(key=lambda x: int(number_pattern.search(x).group(1)))

# Store the output in a list for logging purposes
outputs = []

# Lists to store mean scores and times for each command
prim10_scores, prim10_times = [], []
sp10_scores, sp10_times = [], []

# Define command templates with placeholders for the file paths
commands = {
    "prim10": ["python", "aligment_to_msa.py", "{file_path}", r"MSA\data\score_matrix.txt"],
    "sp10": ["python", "SP_approxv5.py", "{file_path}", r"MSA\data\score_matrix.txt"]
}

# Regular expression to match the score and time in each output
score_pattern = re.compile(r"(\d+)\n([\d.]+)")

# Run each command for each file in the sorted folder list
for file_path in file_list:
    for label, cmd_template in commands.items():
        # Substitute the file path into the command template
        cmd = [part.replace("{file_path}", file_path) for part in cmd_template]
        
        # Run the command and capture output
        result = subprocess.run(cmd, capture_output=True, text=True)
        full_output = result.stdout + result.stderr
        outputs.append(f"{label} - {file_path}:\n{full_output}")  # Capture full output for logging
        
        # Parse the score and time from the output
        match = score_pattern.search(full_output)
        if match:
            score = int(match.group(1))
            time_taken = float(match.group(2))
            
            # Store the values in the appropriate lists based on the label
            if label == "prim10":
                prim10_scores.append(score)
                prim10_times.append(time_taken)
            elif label == "sp10":
                sp10_scores.append(score)
                sp10_times.append(time_taken)
        
        # Print progress
        print(f"{label} for {file_path} complete at {time.time() - start_time:.2f} seconds")

# Save all outputs to a file for full logging
with open("output_log_mutation.txt", "w") as f:
    for output in outputs:
        f.write(output + "\n")
        f.write("="*40 + "\n")  # Separator for readability

# Print final scores and times for each command
print("List of files processed:", file_list)
print("prim10 scores:", prim10_scores)
print("prim10 times:", prim10_times)
print("sp10 scores:", sp10_scores)
print("sp10 times:", sp10_times)

# Print total elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
