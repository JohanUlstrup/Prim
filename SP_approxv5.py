import sys
import argparse
#from Bio import SeqIO
from itertools import combinations
from global_align_linear import *
from extend_msa import *
import time
###
#to run
# python SP_approxv4.py data\testdata_multiple_short.fasta data\score_matrix.txt

###

# Define function to read FASTA file
# def read_fasta_file(file_path):
#     """
#     Reads a FASTA file and returns a dictionary of sequences.
#     """
#     sequences = {}
#     with open(file_path, "r") as fasta_file:
#         for i, record in enumerate(SeqIO.parse(fasta_file, "fasta"), start=1):
#             sequences[f"seq{i}"] = str(record.seq)
#     return sequences




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

def construct_alignment_strings(alignment_data):
    alignment_strings = {}
    num_sequences = len(alignment_data[0])  # Number of sequences
    
    for i in range(num_sequences):
        sequence_string = ""
        for row in alignment_data:
            sequence_string += row[i]
        alignment_strings[f"seq{i + 1}"] = sequence_string
    print(alignment_strings)
    
    return alignment_strings



MA_ids = []
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




def ensure_extend_is_done_correct(min_span_tree, sequences,sub_matrix):
    
    M = []
    aligment_cost=0
    
    for i in range(len(min_span_tree)):

    
        if MA_ids == []:
            MA_ids.append(min_span_tree[i][0])
            MA_ids.append(min_span_tree[i][1])
            opt_cost, aligned_sequences = global_linear(sequences[min_span_tree[i][0]], sequences[min_span_tree[i][1]], 5, sub_matrix)
            aligment_cost+=opt_cost
            M = aligned_sequences

            continue
        

        opt_cost, aligned_sequences = global_linear(sequences[min_span_tree[i][0]], sequences[min_span_tree[i][1]], 5, sub_matrix)
        aligment_cost+=opt_cost
        A=aligned_sequences

        
        M= extend_msa(M, A,min_span_tree[i][0],min_span_tree[i][1])
        
    return M, aligment_cost




def write_alignment_to_fasta(alignment_strings, output_file):
    with open(output_file, 'w') as file:
        for sequence_id, alignment_string in alignment_strings.items():
            file.write(">" + sequence_id + "\n")
            file.write(alignment_string + "\n")

def main():
    start_time = time.time()
    # Read sequences from input FASTA file
    fasta_file_path = sys.argv[1]
    sequences = read_fasta_file(fasta_file_path)
    #print(sequences)

    #read the scoring matrix in phylip fomat
    phylip_matrix = sys.argv[2]
    sub_matrix = read_phylip_like_matrix(phylip_matrix)
    #print(sub_matrix)
    
  

    # Generate pairwise combinations
    pairwise_combinations = generate_pairwise_combinations(sequences)
    #print(pairwise_combinations)

    # Create a dictionary to store sequences with initial values of 0
    sequence_scores = {seq_id: 0 for seq_id in sequences}
    
    
    #getting the list of alignments
    alignment=[]

    #finding the sequenst with the least distens to the other sequences
    for seqid1, seqid2 in pairwise_combinations:
        alignment_score = global_linear(sequences[seqid1], sequences[seqid2], 5, sub_matrix, hide_alignments=False) 
        #int(alignment_score)
        sequence_scores[seqid2]+= alignment_score[0]
        sequence_scores[seqid1]+= alignment_score[0]

    #print("print seq_score",sequence_scores)

    ### trying somethings diffrent 

    ## create a tree structure
    tree = []
    alignment_cost =0
    min_value = min(sequence_scores)  # Find the minimum once

    for i in sequence_scores:
        #print(i)
        if i == min_value:
            continue
        tree.append((min_value, i)) 

    #print(tree)

    msa, aligment_cost=ensure_extend_is_done_correct(tree, sequences, sub_matrix)
    #print("MSA",msa)
    print(aligment_cost)
    # Convert the list of lists into a list of aligned strings for each sequence
    aligned_sequences = [''.join(chars) for chars in zip(*msa)]

    # Output
    #print("aligned_seq",aligned_sequences)

    end_time = time.time()
    elapsed_time = end_time - start_time
    #print(f"Elapsed time: {elapsed_time:.6f} seconds")
    print(elapsed_time)
    ### geting correct aligment score

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
    
    #print("SP_approx score",compute_sp_score(aligned_sequences))







if __name__ == "__main__":
    main()