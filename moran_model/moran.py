import numpy as np

from numpy.random import Generator


class MoranModel:
    def __init__(
            self, 
            N: int, 
            i: int, 
            fitness_A: float,
            fitness_B: float,
            seed = 42
            ):

        self.rng = np.random.default_rng(seed)
        self.initial_N = N
        self.N = N
        self.initial_i = i
        self.i = i
        self.fitness_A = fitness_A
        self.fitness_B = fitness_B
        self.i_history = [self.i]

    def reset(self):
        self.N = self.initial_N
        self.i = self.initial_i
        self.i_history = [self.i]


    def run_until_absorption(self) -> list[int]:
        self.reset() 

        while (self.i > 0 ) & (self.i < self.N): 
            random_number = self.rng.random()
            p_increase = self.probability_i_increase()
            p_decrease = self.probability_i_decrease()

            if random_number < p_increase:
                self.i += 1
            elif random_number < (p_increase + p_decrease):
                self.i -= 1

            self.i_history.append(self.i)

        return self.i_history

    def probability_i_increase(self):
        return self.probability_A_reproduces() * self.probability_B_dies()

    def probability_i_decrease(self):
        return self.probability_B_reproduces() * self.probability_A_dies()

    def probability_i_stays(self):
        return 1 - (self.probability_i_increase() + self.probability_i_decrease())

    def probability_A_reproduces(self):
        return (self.fitness_A*self.i) / (self.fitness_A*self.i + self.fitness_B*(self.N-self.i))

    def probability_B_reproduces(self):
        return (self.fitness_B*(self.N-self.i)) / (self.fitness_A*self.i + self.fitness_B*(self.N-self.i))

    def probability_A_dies(self):
        return self.i / self.N

    def probability_B_dies(self):
        return (self.N-self.i) / self.N

