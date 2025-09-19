#random walk problem using TD now

import numpy as np

values = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
gamma = 1
alpha = 0.1

# TD updated as V_new_(s) = V_old_(s) + (alpha * (R + gamma * V_old_(s')) - V_old_(s)), iteratively

for episode in range(100):
    values_new = values.copy()
    for state in range(5):
        if state == 0:
            if np.random.rand() < 0.5: # left jane
                values_new[state] = values[state] + alpha*((0 + 1*0) - values[state])
            else: # right 
                values_new[state] = values[state] + alpha*((0 + 1*values[state+1]) - values[state])
        elif state == 4:
            if np.random.rand() < 0.5: # left
                values_new[state] = values[state] + alpha*((0 + 1*values[state-1]) - values[state])
            else: # right
                values_new[state] = values[state] + alpha*((1 + 1*0) - values[state])
        else:
            if np.random.rand() < 0.5: # left
                values_new[state] = values[state] + alpha*((0 + 1*values[state-1]) - values[state])
            else: # right
                values_new[state] = values[state] + alpha*((0 + 1*values[state+1]) - values[state])
    values = values_new

print(values)
