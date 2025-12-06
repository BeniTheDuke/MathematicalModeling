import viterbi
from viterbi import Nucleotide, viterbi


sequence : list[Nucleotide] = [
                                Nucleotide.G,
                                Nucleotide.G,
                                Nucleotide.A,
                                Nucleotide.C,
                                Nucleotide.T,
                                Nucleotide.G,
                                Nucleotide.A,
                                Nucleotide.A
                                ]


states = viterbi(sequence)
print(states)
