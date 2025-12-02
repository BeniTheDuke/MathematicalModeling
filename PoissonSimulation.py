import numpy as np




n = 1000 # Number of experiments
lambdaPeoplePerMinute = 5
lambdaEatingWaitingTime = 1/40
duration = 120 


pPersonFinishesInOneMinute = 1 - np.exp(-lambdaEatingWaitingTime)


results : list[int]= []


i :int = 0
for i in range(n):
    peopleCurrently : int = 0
    
    for _ in range(duration):


        # Depending on whether we add or remove the people first, we get a slightly different mean
        # This could be improved by making the timesteps smaller
        peopleCurrently += np.random.poisson(lambdaPeoplePerMinute)

        peopleLeaving :int = 0 
        for _ in range(peopleCurrently):
            if np.random.rand() < pPersonFinishesInOneMinute:
                peopleLeaving += 1
        peopleCurrently -= peopleLeaving

    results.append(peopleCurrently)

print(np.mean(results))
print(np.var(results))
