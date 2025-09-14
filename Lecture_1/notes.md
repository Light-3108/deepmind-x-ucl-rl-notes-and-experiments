Exploration and Exploitation

explore - increase knowledge
exploite - maximize performance based on accuired knowledge


hamro optimal value >= any value at each time step.  (kinaki yesle future ko ni account garxa ni ta, or nagareni true)
so in multi-arm bandit setting, goal is to minimize total regret
![alt text](image.png)

Action value
-> q(a) = expected reward Rt given action At = a. 
1 estimation can be average of previous rewards given At = a. say Qt(a)

now Qt(At) can be defined recursivly
let n = N_t-1_(At)
Qt(At) = (n*Q_t-1 + Rt) / n+1
       = (n*Q_t-1 /n+1)  + Rt/n+1
       =  ..               + (Rt - Q_t-1 + Q_t-1)/n+1
       = Qt-1(n+1)/n+1 + (1/n+1)(Rt - Qt-1)
       = Qt-1 + alpha*(Rt- Qt-1)

![alt text](image-1.png)

can be thought as adding or subtracting on our previous expected value based on error and the learning rate, 
here learning rate decreases with time. 


Algorithms 
1. greedy
