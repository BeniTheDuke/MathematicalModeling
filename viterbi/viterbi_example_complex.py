import sys
import viterbi
from viterbi import Nucleotide, viterbi
from align import align



def char_to_nucleotide(char: str)->Nucleotide:
    match char:
        case "C":
            return Nucleotide.C
        case "T":
            return Nucleotide.T
        case "A":
            return Nucleotide.A
        case "G":
            return Nucleotide.G
        case _:
            raise Exception("Unknown Nucleotide") 

sequence : list[Nucleotide] = []

with open("Sequence_case1.txt", "r") as f:
    sequence_str = "".join(line.strip() for line in f)

    sequence = list(map(char_to_nucleotide, sequence_str))
    
sys.setrecursionlimit(len(sequence)+2) # Because we're doing a lot of recursion

states = viterbi(sequence)
align(sequence, states, 100)
