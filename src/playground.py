from collections import Counter
from pathlib import Path
import re
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import constants
from src import DNAtools

entries = {}
current_key = None
current_sequence = []
parent_path = Path(__file__).resolve().parents[1]
file_path = Path(parent_path / 'data\\testfile.txt')

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if current_key is not None:
                entries[current_key] = ''.join(current_sequence)
                current_sequence = []
            current_key = line[1:]
        else:
            current_sequence.append(line)
    entries[current_key] = ''.join(current_sequence)
            
for entry in entries:
    sequence = entries[entry]
    counted_nucleotides = DNAtools.count_nucleotides(sequence)
    total_nucleotides = sum(counted_nucleotides.values())
    gc_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "C") or (entry == "G")])/total_nucleotides, 5)
    at_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "A") or (entry == "T")])/total_nucleotides, 5)
    entries[entry] = (sequence, at_content, gc_content)
