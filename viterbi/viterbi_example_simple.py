import viterbi
from viterbi import Nucleotide, viterbi
from align import align

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
align(sequence, states)
