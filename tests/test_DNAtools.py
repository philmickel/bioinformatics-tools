from collections import Counter
import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src import DNAtools

class TestFormatSequence(unittest.TestCase):
    def test_valid_string(self):
        sequence = """GATGGAACTTG
            A   CTAC GTAAaTT"""        
        self.assertEqual(DNAtools.format_sequence(sequence), "GATGGAACTTGACTACGTAAATT")
        
    def test_invalid_type(self):
        sequence = True
        with self.assertRaises(Exception):
            DNAtools.format_sequence(sequence)
   
class TestVerifySequence(unittest.TestCase):
    def test_valid_string(self):
        sequence = """GATGGAACTTG
            A   CTAC GTAAaTT"""
        self.assertTrue(DNAtools.verify_sequence(sequence))         
        
    def test_invalid_string(self):
        sequence = "OOBEAR is the best cat."
        self.assertFalse(DNAtools.verify_sequence(sequence))
        
    def test_invalid_type(self):
        sequence = False
        with self.assertRaises(Exception):
            DNAtools.verify_sequence(sequence)

class TestTranscription(unittest.TestCase):
    def test_valid_string(self):
        sequence = "GATGGAACTTGACTACGTAAATT"
        self.assertEqual(DNAtools.transcription(sequence), "GAUGGAACUUGACUACGUAAAUU")
    
    def test_invalid_string(self):
        sequence = "Chai is also a pretty good cat."
        self.assertFalse(DNAtools.transcription(sequence))
        
    def test_invalid_type(self):
        sequence = 15
        with self.assertRaises(Exception):
            DNAtools.transcription(sequence)

class TestCountNucleotides(unittest.TestCase):
    def test_valid_sequence(self):
        sequence = "AAATTCCCCGGGGGGG"
        real_answer = Counter({'A': 3,
                               'T': 2,
                               'C': 4,
                               'G': 7})
        self.assertEqual(DNAtools.count_nucleotides(sequence), real_answer)
    
    def test_invalid_sequence(self):
        sequence = "There's no way you're taking Kairi's heart!"
        self.assertFalse(DNAtools.count_nucleotides(sequence))
     
    def test_invalid_type(self):
        sequence = 159.43
        with self.assertRaises(Exception):
            DNAtools.count_nucleotides(sequence)
  
class TestGetReverseCompliment(unittest.TestCase):
    def test_valid_sequence(self):
        sequence = "AAAACCCGGT"
        answer = "ACCGGGTTTT"
        self.assertEqual(DNAtools.get_reverse_compliment(sequence), answer)

    def test_invalid_sequence(self):
        sequence = "My sanctuary"
        self.assertFalse(DNAtools.get_reverse_compliment(sequence))
        
    def test_invalid_type(self):
        sequence = type(341)
        with self.assertRaises(Exception):
            DNAtools.get_reverse_compliment(sequence)

class TestGetContentPercent(unittest.TestCase):
    def test_valid_sequence(self):
        sequence = """>Rosalind_6404
            CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
            TCCCACTAATAATTCTGAGG
            >Rosalind_5959
            CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
            ATATCCATTTGTCAGCAGACACGC
            >Rosalind_0808
            CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
            TGGGAACCTGCGGGCAGTAGGTGGAAT"""
        answer = {
            "Rosalind_6404": ("CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG", 46.25000, 53.75000),
            "Rosalind_5959": ("CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC", 46.42857, 53.57143),
            "Rosalind_0808": ("CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT", 39.08046, 60.91954)}
        
    def test_invalid_sequence(self):
        sequence = "PARAPPATHARAPPA"
        self.assertFalse(DNAtools.get_content_percent(sequence))

    def test_invalid_type(self):
        sequence = type(195.4)
        with self.assertRaises(Exception):
            DNAtools.get_content_percent(sequence)
            

if __name__ == "__main__":
    unittest.main()