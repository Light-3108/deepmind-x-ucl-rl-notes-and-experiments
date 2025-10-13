from audioop import reverse
from pyparsing import deque
from Environments.four_rooms import SimpleEnv
from minigrid.wrappers import FullyObsWrapper
import numpy as np
import matplotlib.pyplot as plt

# using epsilon greedy 
alpha = 0.01 #optimal alpha for td
gamma = 0.99
epsilon = 0.9
lamda = 0.9
values = {}
save_rewards = []
max_steps = 5e4
seen_frames = 0
rollouts = 0
env = SimpleEnv()
# env = FullyObsWrapper(env)

while seen_frames < max_steps:
    done = False
    epsilon = max(0.1, epsilon * 0.99) 
    obs, info = env.reset()

    states = []
    actions = []
    next_states = []
    rewards = []
    save_lamdas = []
    cnt = 0
    while not done:
        save_lamdas.append(lamda*(1-lamda)**cnt)
        cnt += 1
        pos = env.agent_pos
        dir = env.agent_dir
        obs = (pos[0], pos[1], dir)
        if np.random.rand() < epsilon:
            action = np.random.randint(0,3)
        else:
            # get action using policy
            # obs = just agent position and direction vaye pugxa

            q_values = [values.get((obs, a), 0) for a in range(3)]
            max_q = max(q_values)
            action = np.random.choice([a for a, q in enumerate(q_values) if q == max_q])
        
        next_obs, reward, terminated, truncated, info = env.step(action)
        states.append(obs)
        rewards.append(reward)
        actions.append(action)
        pos = env.agent_pos
        dir = env.agent_dir
        obs = (pos[0], pos[1], dir)
        next_states.append(obs)
        done = terminated or truncated
        seen_frames += 1
        if done:
            save_rewards.append(reward)
            break

    G_t_lamda = save_lamdas[-1]*reward
    for i in reversed(range(len(rewards)-1)): 
        a = actions[i]
        values[(states[i], a)] = values.get((states[i], a), 0) + alpha * (G_t_lamda - values.get((states[i], a), 0))
        if i == 0: 
            break

        q_values = [values.get((obs, a), 0) for a in range(3)]
        max_q = max(q_values)
        action = np.random.choice([a for a, q in enumerate(q_values) if q == max_q])
        

        G_t_lamda = rewards[i-1] + gamma*((1 - lamda)*values.get((next_states[i], action), 0) + lamda*G_t_lamda)
    print(f'Rollout: {rollouts}, Total seen frames: {seen_frames}, Epsilon: {epsilon:.3f}, Reward: {reward}')
    rollouts += 1

#save the values dictionary
np.save('monte_values_alpha_0.1.npy', values)

# plot reward vs episode 
plt.plot(save_rewards)
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Reward vs Episode (Monte-carlo backup, alpha=0.01)')
plt.savefig('reward_vs_episode_monte_alpha_0.01.png')
plt.show()