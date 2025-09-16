import numpy as np
# let the reward of any transition be -1
# policy is uniformly random
gamma = 0.9
mat = np.zeros((4,4))

for _ in range(1000):
    for i in range(4):
        for j in range(4):
            if (i == 0 and j == 0) or (i == 3 and j == 3):
                continue
            a = 0
            b = 0
            c = 0
            d = 0
            if i > 0:
                a = -1 + gamma * mat[i-1][j]
            if i < 3:
                b = -1 + gamma * mat[i+1][j]
            if j > 0:
                c = -1 + gamma * mat[i][j-1]
            if j < 3:
                d = -1 + gamma * mat[i][j+1]
            mat[i][j] = (a + b + c + d) / 4

print(mat)
