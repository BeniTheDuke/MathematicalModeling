from enum import Enum
import numpy as np
from typing import Optional

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
    previous_step: Optional["Step"] = None
    max_v_in_rich : float
    max_v_in_poor: float
    rich_comes_from : State
    poor_comes_from : State


    def Backtrack(self, states: list[State], current_state: State) -> list[State]:
        if self.previous_step is None:
            return states

        state_of_previous: State

        if current_state == State.RICH:
            state_of_previous = self.rich_comes_from
        else: 
            state_of_previous = self.poor_comes_from

        states.insert(0, state_of_previous)

        return self.previous_step.Backtrack(states, state_of_previous)



steps: list[Step] = []

# initialize
current_step = Step()
current_step.max_v_in_rich = INITIAL_P_RICH * EMISS_MAT[State.RICH.value][sequence[0].value] 
current_step.max_v_in_poor = INITIAL_P_POOR * EMISS_MAT[State.POOR.value][sequence[0].value] 

for i in range(1, len(sequence)):
    nucleotide = sequence[i]

    vBeforeRichNowRich = current_step.max_v_in_rich * TRANS_MAT[State.RICH.value][State.RICH.value] * EMISS_MAT[State.RICH.value][nucleotide.value]
    vBeforePoorNowRich = current_step.max_v_in_poor * TRANS_MAT[State.POOR.value][State.RICH.value] * EMISS_MAT[State.RICH.value][nucleotide.value]

    vBeforeRichNowPoor = current_step.max_v_in_rich * TRANS_MAT[State.RICH.value][State.POOR.value] * EMISS_MAT[State.POOR.value][nucleotide.value]
    vBeforePoorNowPoor = current_step.max_v_in_poor * TRANS_MAT[State.POOR.value][State.POOR.value] * EMISS_MAT[State.POOR.value][nucleotide.value]

    new_step: Step = Step()
    new_step.previous_step = current_step

    if vBeforeRichNowRich > vBeforePoorNowRich:
        new_step.max_v_in_rich = vBeforeRichNowRich
        new_step.rich_comes_from = State.RICH
    else:
        new_step.max_v_in_rich = vBeforePoorNowRich
        new_step.rich_comes_from = State.POOR


    if vBeforeRichNowPoor > vBeforePoorNowPoor:
        new_step.max_v_in_poor = vBeforeRichNowPoor
        new_step.poor_comes_from = State.RICH
    else:
        new_step.max_v_in_poor = vBeforePoorNowPoor
        new_step.poor_comes_from = State.POOR

    current_step = new_step;


# Initialize backtracking
state: State

if current_step.max_v_in_rich >= current_step.max_v_in_poor:
    state = State.RICH
else:
    state = State.POOR

states = [state]

# Backtracking
current_step.Backtrack(states, state)
print(states)
