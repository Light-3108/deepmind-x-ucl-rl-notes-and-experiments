# problem
# 5 states, a,b,c,d,e
# uniform random transition (0.5 left, 0.5 right)
# right to the e is +1 reward
# left to the a is 0 reward
# every other transition -> reward = 0
# initial values v(s) = 0.5

import numpy as np

values = np.array([0.5, 0.5, 0.5, 0.5, 0.5])
gamma = 1


# Dp updated as E(R + gamma*V(s')), iteratively

for episode in range(100):
    values_new = values.copy()
    for state in range(5):
        if state == 0:
            values_new[state] = ((0 + 1*0) + (0 + 1*values[state+1]))*0.5
        elif state == 4:
            values_new[state] = ((0 + 1*values[state-1]) + (1 + 1*0))*0.5
        else:
            values_new[state] = ((0 + 1*values[state-1]) + (0 + 1*values[state+1]))*0.5
    values = values_new

print(values)

# after the evaluation using dynamic programming
# we got the true values for this uniform policy 
# which is
# [0.16666667, 0.33333333, 0.5,        0.66666667, 0.83333333]