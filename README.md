# 🧬 FASTA File Analyzer

A beginner-friendly bioinformatics project built with Python to analyze DNA sequences stored in FASTA files. This tool reads multiple sequences, calculates basic sequence statistics, identifies the longest and shortest sequences, and searches for specific DNA motifs.

## ✨ Features

- **FASTA File Reading:** Reads multiple DNA sequences from a FASTA file.
- **DNA Validation:** Checks whether sequences contain only valid DNA bases (`A`, `T`, `G`, and `C`).
- **Sequence Length:** Calculates the length of each DNA sequence.
- **GC Content:** Calculates the percentage of guanine (`G`) and cytosine (`C`) bases.
- **AT Content:** Calculates the percentage of adenine (`A`) and thymine (`T`) bases.
- **Longest Sequence:** Identifies the longest valid DNA sequence.
- **Shortest Sequence:** Identifies the shortest valid DNA sequence.
- **Average Length:** Calculates the average length of valid DNA sequences.
- **DNA Motif Search:** Finds all occurrences of a user-provided motif, including overlapping matches.
- **Error Handling:** Handles missing files, malformed FASTA headers, and invalid or empty DNA sequences.

## 🛠️ Technologies Used

- Python 3
- `collections.Counter`
- File handling
- Lists and dictionaries
- Functions and loops
- Exception handling
- Basic bioinformatics concepts

## 📂 Project Structure

```text
fasta-analyzer/
├── fasta_analyzer.py
├── sample.fasta
└── README.md
```

`sample.fasta` is an example input file that you can create to test the program.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your GitHub username and repository name.

### 2. Navigate to the project directory

```bash
cd YOUR-REPOSITORY
```

### 3. Prepare a FASTA file

Create a file named `sample.fasta` with the following content:

```text
>seq1
ATGCGCATTA
>seq2
GGCCATATGC
>seq3
ATATATGGCC
```

Each sequence begins with a header starting with `>`, followed by its DNA sequence. A sequence may also span multiple lines.

### 4. Run the program

Make sure Python 3 is installed, then run:

```bash
python3 fasta_analyzer.py
```

Enter the FASTA filename when prompted:

```text
sample.fasta
```

Next, enter a DNA motif to search for, such as:

```text
ATG
```

## 🧪 Example Output

For the sample sequences above, the report will include results similar to these:

```text
===== FASTA ANALYSIS REPORT =====

Sequence ID: seq1
Sequence: ATGCGCATTA
Length: 10 bases
GC%: 40.00%
AT%: 60.00%

Sequence ID: seq2
Sequence: GGCCATATGC
Length: 10 bases
GC%: 50.00%
AT%: 50.00%

Sequence ID: seq3
Sequence: ATATATGGCC
Length: 10 bases
GC%: 50.00%
AT%: 50.00%

===== SUMMARY =====
Longest sequence: seq1 (10 bases)
Shortest sequence: seq1 (10 bases)
Average length: 10.00 bases
Total valid sequences: 3

===== MOTIF SEARCH: ATG =====
seq1 - motif found at positions: [1]
seq2 - motif found at positions: [7]
seq3 - motif not found.
```

_Note: When multiple sequences share the same longest or shortest length, Python's `max()` and `min()` return the first matching sequence._

## 🧬 Bioinformatics Concepts Demonstrated

This project applies several fundamental bioinformatics concepts:

- Nucleotide composition analysis
- GC and AT content calculation
- DNA sequence validation
- Sequence length statistics
- Motif and pattern matching
- One-based biological sequence positions
- Handling multiple sequences in FASTA format

## 🎯 Learning Objectives

This project helped me practice:

- Reading and processing biological sequence files
- Working with Python functions, lists, dictionaries, and sets
- Using `Counter` to count nucleotides
- Handling errors using `try` and `except`
- Searching for patterns in DNA sequences
- Applying Python programming to real-world bioinformatics problems

## 🔮 Future Improvements

Possible enhancements include:

- Support for RNA sequences and ambiguous nucleotide symbols
- Exporting analysis reports to CSV or text files
- Counting nucleotide frequencies across all sequences
- Finding the most frequent k-mers
- Approximate motif matching using Hamming distance
- Adding automated unit tests
- Building a simple web interface

## 👩‍💻 Author

Created as a learning project to develop Python programming skills and explore practical bioinformatics.

## 📄 License

This project is open source. You may add an MIT License if you want others to reuse, modify, and distribute your code under its terms.
