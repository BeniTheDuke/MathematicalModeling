from enum import Enum
import numpy as np

class Nucleotide(Enum):
    T = 0
    C = 1
    A = 2
    G = 3

class State(Enum):
    RICH = 0
    POOR = 1

TRANS_MAT = np.array([
    # R    P
    [0.5, 0.5], # R
    [0.6, 0.4]  # P
])

EMISS_MAT = np.array([
    # T    C    A    G
    [0.2, 0.3, 0.2, 0.3],  # R
    [0.3, 0.2, 0.3, 0.2]   # P
])

INITIAL_P_RICH = 0.5
INITIAL_P_POOR = 0.5

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

class Step:
    previous_step: "Step"
    max_probability_in_rich : float
    max_probability_in_poor: float
    rich_comes_from : State
    poor_comes_from : State



steps: list[Step] = []

# initialize
current_step = Step()
current_step.max_probability_in_rich = INITIAL_P_RICH * EMISS_MAT[State.RICH.value][sequence[0].value] 
current_step.max_probability_in_poor = INITIAL_P_POOR * EMISS_MAT[State.POOR.value][sequence[0].value] 

# for i in range(1, len(sequence)):


    
print(current_step.max_probability_in_rich)
print(current_step.max_probability_in_poor)


