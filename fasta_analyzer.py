from collections import Counter

def read_fasta(filename):
    with open(filename, "r") as file:
        sequences = []
        sequence_id = None
        sequence_parts = []
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if sequence_id is not None:
                    sequences.append({
                        "id": sequence_id,
                        "sequence": "".join(sequence_parts)
                    })
            
                header = line[1:].strip()

                if not header:
                    raise ValueError("FASTA header cannot be empty.")

                sequence_id = header.split()[0]
                sequence_parts = []
                
            else:
                if sequence_id is None:
                    raise ValueError(
                        "Sequence data found before a FASTA header."
                    )
                sequence_parts.append(line.upper())

        if sequence_id is not None:
            sequences.append({
                 "id": sequence_id,
                 "sequence": "".join(sequence_parts)
                        })
    return sequences

def sequence_analyzer(sequence):
    counts = Counter(sequence) 
    length = len(sequence)  

    if length == 0:
        return{
            "length": 0,
            "gc_percent": 0.0,
            "at_percent": 0.0
        }

    gc_percentage = (counts["G"] + counts["C"]) / length * 100
    at_percentage = (counts["A"] + counts["T"]) / length * 100

    return {
    "length": length,
    "gc_percent": gc_percentage,
    "at_percent": at_percentage
    }

def find_motif(sequence, motif):
    sequence = sequence.upper()
    motif = motif.upper()

    positions = []
    start = 0

    if not motif:
        return positions

    while True:
        position = sequence.find(motif, start)

        if position == -1:
                    break
        
        positions.append(position + 1)
        start = position + 1

        
    return positions

def analyze_fasta():
     filename = input("Enter FASTA filename: ").strip()

     try:
          sequences = read_fasta(filename)
     except FileNotFoundError:
          print("Error: FASTA file not found")
          return
     except (ValueError, OSError) as error:
          print(f"Error reading FASTA file: {error}")
          return
     if not sequences:
          print("No sequences found in this file")
          return

     print("\n===== FASTA ANALYSIS REPORT =====")

     valid_sequences = []

     for item in sequences:
           
          sequence = item["sequence"]

          if not sequence or not set(sequence).issubset(
               {"A", "T", "G", "C"}):
               print(f"\nSkipping {item['id']}: invalid or empty DNA.")
               continue

          valid_sequences.append(item)
          
          result = sequence_analyzer(item["sequence"])

          print(f"\nSequence Id: {item['id']}")
          print(f"Sequence: {item['sequence']}")
          print(f"Length: {result['length']} bases")
          print(f"GC%: {result['gc_percent']:.2f}")
          print(f"AT%: {result['at_percent']:.2f}")
          print("\n")

     if not valid_sequences:
        print("\nNo valid DNA sequences to analyze.")
        return

     longest = max(valid_sequences, key= lambda item: len(item["sequence"]) )

     shortest = min(valid_sequences, key=lambda item: len(item["sequence"]))

     total_length = sum(
        len(item["sequence"]) for item in valid_sequences
    )

     average_length = total_length / len(valid_sequences)

     print("\n===== SUMMARY =====")
     print(
          f"Longest sequence: {longest['id']} "
          f"({len(longest['sequence'])} bases)"
        )
     print(
          f"Shortest sequence: {shortest['id']} "
          f"({len(shortest['sequence'])} bases)"
        )
     print(
          f"Average length: {average_length:.2f} bases")
     print(
          f"Total valid sequences: {len(valid_sequences)}")

     motif = input("\n Enter your motif: ").strip().upper()

     if not motif or not set(motif).issubset(
          {"A", "T", "G", "C"}):
          print("Either motif is empty or invalid")
          return

     for item in valid_sequences:
      positions = find_motif(item["sequence"], motif)

     if positions:
            print(f"{item['id']} - motif found at positions: {positions}")
     else:
            print(f"{item['id']} - motif not found.")

if __name__ == "__main__":
     analyze_fasta()
     
     

     
    
          
 

        

