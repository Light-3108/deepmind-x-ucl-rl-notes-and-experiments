## MDP 

In mdp state s contains all relevant information to make decisions

Hence history can be thrown away or not needed

![alt text](image.png)

Connection between value function and state action value

![alt text](image-1.png)

sum the state action value weighted by the probability of taking that action

optimal value function -> max value function over all policies. 

Theorem:

1. There exists an optimal policy that is better or equal to all other policies
2. All optimal policies achieves optimal value function
3. All optimal policies achieves optimal action value function


If we have optimal action value function, we can have optimal policy

just take action which leads to highest action value

![alt text](image-2.png)
 
---

## Bellman Equations

value function and state value function can be written recursively

![alt text](image-3.png)

Sum (r + gamma*v(s')) weighted by every possible transitions p(r,s' | s, a) * 

weighted by taking that action pie(a | s)

First action ko probability ani tespaxi transition ko probability, dubai hunu paryo

so mulitply

similary for action values

![alt text](image-4.png)

same value function ko jastai equation ho

convert v_pie(s') to q_pie(s',a') by weighting over action and

we don't have to weight over action in front, becuase action is fixed or already choosen in action value. 


__Bellman's Expectation Equations__

![alt text](image-5.png)

__Bellman's Optimal Equations__

Instead of weighting over actions, take max over actions

![alt text](image-6.png)

---

## Bellman's Equation in Matrix form

![alt text](image-7.png)

Here v is the value function of all possible states [v[s1], v[s2], .... ]^T

r^pie = expected immediate reward following policy pie

p^pie = state transition matrix under policy pie

it's a linear equation, can be solved directly for small problems

![alt text](image-8.png)

Example for a uniform policy with 2*2 matrix where goal is on buttom right.
we can solve as

![alt text](image-9.png)


## Dynamic Programming

Collection of algorithms which can be used to compute optimal policies given the perfect model of the environment as MDP

Consists of 

1. Policy Evaluation
2. Policy Improvement

## Policy Evaluation

Algorithm

![alt text](image-10.png)

Acting greedily on the value of uniform policy can give optimal policy, but not always.

![alt text](image-11.png)


What we can do is

1. Evaluate policy of some uniform policy
2. you will get relatively good value function (after doing evaluation)
3. Now make new policy from the evaluated value function
4. Now evaluate this new policy
5. Repeat (in this way we reach optimal policy)

v_pie_new(s) >=  v_pie(s), for all s. so our value function and policy becomes better with each iterations. 

![alt text](image-12.png)

up arrow is evaluation

down arrow is greedyfication

We can repeat evaluation and greedyfication improving each time to reach optimal policy. 




