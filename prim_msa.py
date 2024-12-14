import sys
#from Bio import SeqIO
from itertools import combinations
from lazy_prim import *
#from Eager_prim import *
import time




###
"""

to run this code 
python aligment_to_matrix.py MSA\data\testdata_short.fasta MSA\data\score_matrix.txt


 python aligment_to_msa.py MSA\data\testdata_many_short.fasta MSA\data\score_matrix.txt
"""
###

####

#reading files into the script

####

#read fasta files 
def read_fasta_file(fasta_file):
    sequences = {}
    with open(fasta_file, 'r') as file:
        sequence_id = None
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_id:
                    sequences[sequence_id] = sequence
                sequence_id = line[1:]
                sequence = ""
            else:
                sequence += line
        if sequence_id:
            sequences[sequence_id] = sequence
    return sequences

# Read the .txt file containing the substitution matrix
# uses the phylip-like format
def read_phylip_like_matrix(matrix_file):
    matrix = {}
    with open(matrix_file, 'r') as file:
        #num_chars = int(file.readline().strip())
        characters = ['A', 'C', 'G', 'T']
        for char in characters:
            matrix[char] = {}
        for line in file:
            line = line.strip().split()
            char = line[0]
            scores = list(map(int, line[1:]))
            for i, score in enumerate(scores):
                matrix[char][characters[i]] = score
    return matrix




# Define functions to generate pairwise combinations and run alignment script
def generate_pairwise_combinations(sequences):
    
    #Generates all possible pairwise combinations of sequences.
    pairwise_combinations = list(combinations(sequences, 2))
    return pairwise_combinations



def global_linear_pairwise_aligment(A, B, g, sub_matrix):
    A = A.upper()
    B = B.upper()
    
    n = len(A)
    m = len(B)
    
    # Initialize DP table with dimensions (n+1) x (m+1)
    T = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the first column (aligning A with gaps)
    for i in range(1, n + 1):
        T[i][0] = i * g
    
    # Fill the first row (aligning B with gaps)
    for j in range(1, m + 1):
        T[0][j] = j * g
    
    # Fill the rest of the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = T[i-1][j-1] + sub_matrix[A[i-1]][B[j-1]]
            insert = T[i][j-1] + g
            delete = T[i-1][j] + g
            T[i][j] = min(match, insert, delete)
    
    opt_cost = T[n][m]
    
    # Iterative traceback to construct the alignment as a list of pairs
    aligned_sequences = []
    i, j = n, m
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and T[i][j] == T[i-1][j-1] + sub_matrix[A[i-1]][B[j-1]]:
            aligned_sequences.append([A[i-1], B[j-1]])
            i -= 1
            j -= 1
        elif i > 0 and T[i][j] == T[i-1][j] + g:
            aligned_sequences.append([A[i-1], '-'])
            i -= 1
        else:
            aligned_sequences.append(['-', B[j-1]])
            j -= 1
    
    # Since we built the alignment from the end, reverse the list
    aligned_sequences.reverse()
    
    return opt_cost, aligned_sequences





######## creating a matrix to store the aligmnet values in #######
# Initialize a matrix with zeros
def initialize_matrix(sequence_ids):
    n = len(sequence_ids)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    return matrix


def fill_alignment_matrix(sequences, pairwise_combinations, sub_matrix):
    sequence_ids = list(sequences.keys())
    n = len(sequence_ids)
    matrix = initialize_matrix(sequence_ids)  # Initialize your matrix here
    alignment_scores = []  # List to store alignment scores

    for seqid1, seqid2 in pairwise_combinations:
        i = sequence_ids.index(seqid1)
        j = sequence_ids.index(seqid2)
        alignment_score, _ = global_linear_pairwise_aligment(sequences[seqid1], sequences[seqid2], 5, sub_matrix)
        
        # Assign the score to the matrix (symmetric assignment)
        matrix[i][j] = alignment_score
        matrix[j][i] = alignment_score
        
        # Add the alignment score to the list
        alignment_scores.append(alignment_score)
        
    return matrix, alignment_scores

####
 # >constructing MSA 
####
MA_ids = []

#conventing the fomat so it goes from [[]]
def convert_aligment_to_corect_fomat(aligned_sequences):
    return

def extend_msa(M, A,seq_id1,seq_id2):
    MA = []
    i = 0
    j = 0
    MA_ids.append(seq_id2)
    # Determine location of seq_id1 in MA
    if seq_id1 in MA_ids:
        seq_loc = MA_ids.index(seq_id1)
    else:
        return  "ERRROR case where the sequence you are trying to align is not found in MA_ids"
    
    

    while i < len(M) and j < len(A):
        # Invariant: (1) MA is a valid merge of all columns before column i in M
        # and all columns before column in A, and (2) the first row of M and A up
        # to (but not including) column i and j respectively is the same string
        # if gaps are removed.
    
        if M[i][seq_loc] == '-' and A[j][0] == '-':
            # Case 1: The next column in MA is column i in M extended with the second symbol
            # in column j in A.
            M[i].append(A[j][1])
            MA.append(M[i])
            i = i + 1
            j = j + 1

        elif M[i][seq_loc] == '-' and A[j][0] != '-':
            # Case 2: A[j][0] is a character, so the second symbol in column j in A, A[j][1],
            # must be in the column of MA that is the column in M where the first symbol corresponds
            # to A[j][0]. By the invariant, this column in M is the next column in M, where the first
            # symbol is a character, so we just moved forward in M until we find this column.
            M[i].append('-')
            MA.append(M[i])
            i = i + 1

        elif M[i][seq_loc] != '-' and A[j][0] == '-':
            # Case 3: M[i][0] is a character, so column i in M must be in the column of MA that also
            # contains the second symbol from the column in A, where the first symbol is the character
            # corresponding to M[i][0]. By the invariant, this column in A is the next column in A,
            # where the first symbol is a character, so we just add columns from A to MA until we
            # find this column.
            c = ['-']*len(M[i])
            c.append(A[j][1])
            MA.append(c)
            j = j + 1

        elif M[i][seq_loc] != '-' and A[j][0] != '-':
            # Case 4: By the invariant the characters M[i][0] and A[j][0] are at the same position
            # in the string spelled by the row of M and A if gaps are removed. The next column in
            # MA is thus column i in M extended with the second symbol in column j in A.
            M[i].append(A[j][1])
            MA.append(M[i])
            i = i + 1
            j = j + 1

    if i < len(M):
        # add the remaining columns of M to MA
        while i < len(M):
            M[i].append('-')
            MA.append(M[i])
            i = i + 1
        
    if j < len(A):
        # add the remaining columns of A to MA
        k = len(MA[-1])
        while j < len(A):
            c = ['-']*(k-1)
            c.append(A[j][1])
            MA.append(c)
            j = j + 1

    return MA




# Testing with the given sequences
def ensure_extend_is_done_correct(min_span_tree, sequences,sub_matrix):
    
    M = []
    
    for i in range(len(min_span_tree)):

    
        if MA_ids == []:
            MA_ids.append(min_span_tree[i][0])
            MA_ids.append(min_span_tree[i][1])
            opt_cost, aligned_sequences = global_linear_pairwise_aligment(sequences[min_span_tree[i][0]], sequences[min_span_tree[i][1]], 5, sub_matrix)
            M = aligned_sequences

            continue
        

        opt_cost, aligned_sequences = global_linear_pairwise_aligment(sequences[min_span_tree[i][0]], sequences[min_span_tree[i][1]], 5, sub_matrix)
        A=aligned_sequences

        
        M= extend_msa(M, A,min_span_tree[i][0],min_span_tree[i][1])
        
    return M

####

# construct fasta file 

####

def extract_sequences_from_alignment(alignment):
    # Number of sequences is determined by the length of each inner list
    num_sequences = len(alignment[0])
    
    # Initialize a list of empty strings, one for each sequence
    sequences = ['' for _ in range(num_sequences)]
    
    # Iterate over each position in the alignment
    for position in alignment:
        for i in range(num_sequences):
            sequences[i] += position[i]
    
    return sequences


def write_fasta(sequences, names,mst_cost, output_file):
    with open(output_file, 'w') as f:
        f.write(f"alignment score: {mst_cost}\n")
        for name, sequence in zip(names, sequences):
            f.write(f">{name}\n")
            # Write the sequence in FASTA format, with 60 characters per line
            for i in range(0, len(sequence), 60):
                f.write(sequence[i:i+60] + '\n')
                f.write( '\n')


###

#       test

###

def test_multiple_aligment(sequences,alignment,min_span_tree,MA_ids,sub_matrix):
    # Initialize the flag to True. It will be set to False if any alignment doesn't match.
    all_identical = True

    # Create a mapping from sequence IDs to their indices in MA_ids for efficient lookup
    id_to_index = {seq_id: idx for idx, seq_id in enumerate(MA_ids)}
    
    # Iterate over each pair in the minimum spanning tree
    for pair in min_span_tree:
        seq1 = pair[0]
        seq2 = pair[1]
 
               
        # Perform pairwise alignment (assuming global_linear_pairwise_alignment is defined)
        opt_cost, aligned_sequences = global_linear_pairwise_aligment(sequences[seq1], sequences[seq2], 5, sub_matrix)
        

        
        # Find indices of seq1 and seq2 in MA_ids
        try:
            index1 = id_to_index[seq1]
            index2 = id_to_index[seq2]
        except KeyError as e:
            print(f"Error: Sequence ID '{e.args[0]}' not found in MA_ids.")
            continue
        
        # Extract aligned sequences from msa_alignment using the found indices
        aligned_seq1 = alignment[index1]
        aligned_seq2 = alignment[index2]
        

        aligned_pairs_MSA = []
        for char1, char2 in zip(aligned_seq1, aligned_seq2):
            aligned_pairs_MSA.append([char1, char2])

        # Filter out ['-', '-'] pairs from aligned_pairs_MSA
        filtered_pairs_MSA = [pair for pair in aligned_pairs_MSA if pair != ['-', '-']]
        



        # Compare the two filtered lists directly
        if filtered_pairs_MSA == aligned_sequences:
            continue
            
        else:
            all_identical = False 
            

    return all_identical







####

#main

###

def main():
    start_time = time.time()
    # Read sequences from input FASTA file
    fasta_file_path = sys.argv[1]
    sequences = read_fasta_file(fasta_file_path)
 

    #read the scoring matrix in phylip fomat
    phylip_matrix = sys.argv[2]
    sub_matrix = read_phylip_like_matrix(phylip_matrix)


    # Generate pairwise combinations
    pairwise_combinations = generate_pairwise_combinations(sequences)
    #print(pairwise_combinations)

    pairwise_alignment_lsit =[]
    alignment_score_matrix=initialize_matrix(pairwise_combinations)
    

    # Fill the alignment score matrix
    alignment_score_matrix, list_of_scores = fill_alignment_matrix(sequences, pairwise_combinations, sub_matrix)


    ##tuned of for testing perpupeses

   

    # Extract the names of the sequences
    sequence_ids = list(sequences.keys())
   
    
    ## using the lazy prim algorithm O=(E*log(E)) called form lazy_prim.py
    mst_cost, mst_edges = lazy_prim(0, alignment_score_matrix)
    
    
    #to get the information out of my class
    min_span_tree=[]
    for edge in mst_edges:
        
        min_span_tree.append([sequence_ids[edge.start],sequence_ids[edge.end],edge.cost])
    #print(min_span_tree)
    #print(alignment_score_matrix)
    
    
    #making and extending MSA
    msa=ensure_extend_is_done_correct(min_span_tree, sequences, sub_matrix)
    
    
    ##

    # testing that the aligment is correct 

    ##
   
    # Extract sequences from alignment
    alignment=extract_sequences_from_alignment(msa)
   
    
    #test= test_multiple_aligment(sequences,alignment,min_span_tree,MA_ids,sub_matrix)

    
    end_time = time.time()
    elapsed_time = end_time - start_time
    #print(f"Elapsed time: {elapsed_time:.6f} seconds")
    # write fasta file
    
    # Define output file name
    output_file = "sequences.fasta"

    # Write sequences to FASTA file
    #write_fasta(alignment, MA_ids,mst_cost, output_file)
    #print(alignment)
    #print(f"FASTA file '{output_file}' has been created.")
    
    #print("mst_cost:",mst_cost)
    #print(alignment)
    #print(sequences)
  


    cost = [[0, 5, 2, 5, 5],  # A
        [5, 0, 5, 2, 5],  # C
        [2, 5, 0, 5, 5],  # G
        [5, 2, 5, 0, 5],  # T
        [5, 5, 5, 5, 0]]  #-'

    dict_str2seq = {'a':0, 'c':1, 'g':2, 't':3, 'A':0, 'C':1, 'G':2, 'T':3, '-':4, 'N':0, 'R':0, 'S':0}

    def str2seq(s):
        """
        Convert a string sequence to a list of indices based on dict_str2seq.
        """
        try:
            seq = [dict_str2seq[c] for c in list(s)]
            return seq
        except KeyError as e:
            print("ERROR: Illegal character", e, "in input string.")
            sys.exit(1)

    def compute_sp_score(sequences):
        """
        Computes the sum-of-pairs (SP) score for a list of aligned sequences.
        """
        # Convert each sequence string to a list of indices
        row = [str2seq(s) for s in sequences]

        # Check that all sequences are of equal length
        for seq in row:
            if len(seq) != len(row[0]):
                print("ERROR: All sequences must have the same length.")
                sys.exit(1)

        # Compute the sum-of-pairs score
        score = 0
        for i in range(len(row)):
            for j in range(i + 1, len(row)):
                for c in range(len(row[i])):
                    score += cost[row[i][c]][row[j][c]]
        return score
    
    #print("prim_MSA",compute_sp_score(alignment))
    print(compute_sp_score(alignment))
    print(elapsed_time)






# Add this block to call main() when the script is executed
if __name__ == "__main__":
    main()

