# Multiple Sequence Alignment Algorithms

This repository contains scripts and test data for comparing and running multiple sequence alignment (MSA) algorithms, including **Prim-MSA**, **SP-Exact**, and **SP-Approx**.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
   - [Running Prim-MSA](#running-prim-msa)
   - [Running SP-Exact](#running-sp-exact)
   - [Running SP-Approx](#running-sp-approx)
4. [Testing of algorithms](#testing_algorithms)


---

## Project Overview

This repository provides scripts for running various MSA algorithms:
- **Prim-MSA**: A heuristic MSA algorithm leveraging Prim's algorithm for constructing minimum spanning trees.
- **SP-Exact**: An exact MSA algorithm with exponential time complexity.
- **SP-Approx**: A heuristic algorithm for faster, approximate alignments.

Additionally, the repository includes test datasets and scripts for evaluating the performance of these algorithms.

---

## Setup Instructions

1. Ensure you have Python 3.10.14 installed.
2. Clone this repository to your local machine:


## Usage
### Running Prim-MSA
The `prim_msa.py` script runs the Prim-MSA algorithm. Ensure the `prim.py` script is in the same directory.

**Command**:
```bash
python prim_msa.py <data.fasta> <score_matrix.txt>
```
###Running SP-Exact
The `sp_exact_3.py` script runs the SP-Exact algorithm.

Command:
```bash
python sp_exact_3.py <data.txt> -g <gap_penalty> -m <score_matrix.txt>
```
Running SP-Approx
The `SP_approxv5.py` script runs the SP-Approx algorithm. Use the following command:

Command:
```bash
python SP_approxv5.py <data.fasta> <score_matrix.txt>
```
## Data Simulation

The data used for testing and mutation was simulated using the script `simulate_data_v2.py`. To run the script and generate mutated data, follow the instructions below.

### Usage of `simulate_data_v2.py`
1. **Open the Script**:
   - Open `simulate_data_v2.py` in your preferred text editor or IDE.

2. **Modify File Path**:
   - Change the `path` variable to the location of the input FASTA file you want to mutate. The script reads the sequence data from this file.
   
   ```python
   path = r"Your\\path\\to\\file"
   filename = "gene.fna"

Command:
```bash
simulate_data_v2.py
```

### `mutated_fox/`
This folder contains the test data used for all the experiments and algorithm evaluations. The test data is essential for running the different MSA algorithms and includes various datasets for testing alignment quality, performance, and scalability.


### `testing_of_algorithms/`
This folder contains the scripts used to evaluate and test the performance of the MSA algorithms. The testing scripts help automate the process of comparing different algorithms, ensuring consistency across tests, and analyzing results.














