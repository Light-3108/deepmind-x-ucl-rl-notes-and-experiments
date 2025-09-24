# At t = 1 we took action a and got reward 0
# At t = 2 we took action b and got reward 1
# What is P(A3 = a) ?

# def greedy():
# ans = 0
# def epsilon_greedy(epsilon):
# ans = e/2
# def UCB(c):
# ans = 0
# def Thompson_sampling():
# ans = 1/6


# make Beta (1,2) i.e for action a
# make Beta (2,1) i.e for action b
# sample like 50 times and see how many times we get a > b
# P(A3 = a) = P(sample from Beta(1,2) > sample from Beta(2,1))

import numpy as np

alpha_a = 1
beta_a = 2
alpha_b = 2
beta_b = 1

samples1 = np.random.beta(alpha_a, beta_a, 100000)
samples2 = np.random.beta(alpha_b, beta_b, 100000)

p_A3_a = np.mean(samples1 > samples2)
print(p_A3_a)

# Ans : 0.16715 which is nearly 1/6
