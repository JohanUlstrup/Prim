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
4. [Repository Structure](#repository-structure)

---

## Project Overview

This repository provides scripts for running various MSA algorithms:
- **Prim-MSA**: A heuristic MSA algorithm leveraging Prim's algorithm for constructing minimum spanning trees.
- **SP-Exact**: An exact MSA algorithm with exponential time complexity.
- **SP-Approx**: A heuristic algorithm for faster, approximate alignments.

Additionally, the repository includes test datasets and scripts for evaluating the performance of these algorithms.

---

## Setup Instructions

1. Ensure you have Python 3.x installed.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
