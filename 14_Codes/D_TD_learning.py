from Environments.two_rooms import SimpleEnv
from minigrid.wrappers import FullyObsWrapper
import numpy as np
import matplotlib.pyplot as plt

# using epsilon greedy 
alpha = 0.1 #optimal alpha for td
gamma = 0.99
epsilon = 0.9
values = {}
rewards = []
max_steps = 5e4
seen_frames = 0
rollouts = 0
env = SimpleEnv()
# env = FullyObsWrapper(env)

while seen_frames < max_steps:
    done = False
    epsilon = max(0.1, epsilon * 0.99) 
    obs, info = env.reset()
    while not done:
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
        pos = env.agent_pos 
        dir = env.agent_dir
        next_obs = (pos[0], pos[1], dir)
        max_next_q = max([values.get((next_obs, a), 0) for a in range(3)])
        values[(obs,action)] = values.get((obs, action), 0) + alpha * (reward + gamma * max_next_q - values.get((obs, action), 0))
        done = terminated or truncated
        seen_frames += 1
        if done:
            rewards.append(reward)
            break
    print(f'Rollout: {rollouts}, Total seen frames: {seen_frames}, Epsilon: {epsilon:.3f}, Reward: {reward}')
    rollouts += 1

#save the values dictionary
np.save('td_values_alpha_0.1.npy', values)

# plot reward vs episode 
plt.plot(rewards)
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.title('Reward vs Episode (TD Learning, alpha=0.1)')
plt.savefig('reward_vs_episode_td_alpha_0.1.png')
plt.show()