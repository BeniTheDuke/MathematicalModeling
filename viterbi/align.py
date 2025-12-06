from viterbi import Nucleotide, State


def align(sequence: list[Nucleotide], states: list[State], line_length: int = 30):
    """Not part of the algorithm. Just for visualization"""

    sequence_str = "".join(map(nucleotide_to_char, sequence))
    states_str = "".join(map(state_to_char, states))

    for i in range (0, min(len(sequence), len(states)), line_length):
        chunk_a = sequence_str[i:i+line_length]
        chunk_b = states_str[i:i+line_length]
        print(chunk_a)
        print(chunk_b)
        print()


def nucleotide_to_char(nucleotide: Nucleotide)-> str:
    """Not part of the algorithm. Just for visualization"""
    match nucleotide:
        case Nucleotide.T:
            return "T"
        case Nucleotide.C:
            return "C"
        case Nucleotide.A:
            return "A"
        case Nucleotide.G:
            return "G"


def state_to_char(state: State):
    """Not part of the algorithm. Just for visualization"""
    match state:
        case State.RICH:
            return "R"
        case State.POOR:
            return "P"
