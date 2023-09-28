from collections import Counter
import os
from pathlib import Path
import re
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from constants import constants

def format_sequence(sequence):
    if isinstance(sequence, str):
        formatted = re.sub(r"[\n\t\s]*", "", sequence.upper())
        for nucleotide in formatted:
            if nucleotide in constants.nucleotide_dict.keys():
                pass
            else:
                raise Exception("All characters in sequence should be valid DNA or RNA nucleotides.")
        return formatted
    else:
        raise Exception("Input should be a string containing valid DNA or RNA nucleotides.")
    
def transcription(DNA_sequence):      
    formatted_sequence = format_sequence(DNA_sequence)
    return formatted_sequence.replace('T', 'U')
                
def count_nucleotides(sequence):
    formatted_sequence = format_sequence(sequence)
    return Counter(formatted_sequence)

def get_reverse_compliment(sequence):
    formatted_sequence = format_sequence(sequence)
    reverse_sequence = "".join([formatted_sequence[i] for i in range(len(formatted_sequence)-1, -1, -1)])
    return "".join([constants.nucleotide_dict[i][1] for i in reverse_sequence])  

def read_FASTA(file_path):
    entries = {}
    current_key = None
    current_sequence = []
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith('>'):
                for line in file:
                    line = line.strip()
                    if line.startswith(">"):
                        if current_key is not None:
                            entries[current_key] = ''.join(format_sequence(current_sequence))
                            current_sequence = []
                        current_key = line[1:]
                    else:
                        current_sequence.append(line)
                if current_key is not None:
                    entries[current_key] = ''.join(current_sequence)
                return entries
            else:
                raise Exception("File must be a FASTA formatted file.")
    except FileNotFoundError:
        raise Exception(f'The file {file_path} does not exist.')
        
        

def get_content_percent(sequence):
    formatted_sequence = format_sequence(sequence)
    counted_nucleotides = count_nucleotides(formatted_sequence)
    total_nucleotides = sum(counted_nucleotides.values())
    gc_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "C") or (entry == "G")])/total_nucleotides, 5)
    at_content = round(100*sum([counted_nucleotides[entry] for entry in counted_nucleotides if (entry == "A") or (entry == "T")])/total_nucleotides, 5)
    return (at_content, gc_content)
