from collections import Counter
import os
from pathlib import Path
import re
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import constants

def format_sequence(sequence):
    try:
        return re.sub(r"[\n\t\s]*", "", sequence.upper())
    except TypeError:
        print("Sequence needs to be a string.")
    else:
        return False
    
def verify_sequence(sequence):
    formatted_sequence = format_sequence(sequence)
    for nucleotide in formatted_sequence:
        if nucleotide in constants.nucleotide_dict.keys():
            pass
        else:
            return False
    return True

def transcription(DNA_sequence):
    if verify_sequence(DNA_sequence):         
        return DNA_sequence.replace('T', 'U')
                
def count_nucleotides(sequence):
    if verify_sequence(sequence):
        formatted_sequence = format_sequence(sequence)
        return Counter(formatted_sequence)

def get_reverse_compliment(sequence):
    if verify_sequence(sequence):
        reverse_sequence = "".join([sequence[i] for i in range(len(sequence)-1, -1, -1)])
        return "".join([constants.nucleotide_dict[i][1] for i in reverse_sequence])
    


def get_content_percent(file_path):
    # Result is a dictionary with keys of the DNA name, containing entries of (sequence, AT content %, GC content %)
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
                    if verify_sequence(current_sequence):
                        entries[current_key] = ''.join(current_sequence)
                        current_sequence = []
                current_key = line[1:]
            else:
                current_sequence.append(line)
        entries[current_key] = ''.join(current_sequence)
    for entry in entries:
        sequence = entries[entry]
        if verify_sequence(sequence):
            counted_nucleotides = count_nucleotides(sequence)
            total_nucleotides = sum(counted_nucleotides.values())
            gc_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "C") or (entry == "G")])/total_nucleotides, 5)
            at_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "A") or (entry == "T")])/total_nucleotides, 5)
            entries[entry] = (sequence, at_content, gc_content)
    return entries
