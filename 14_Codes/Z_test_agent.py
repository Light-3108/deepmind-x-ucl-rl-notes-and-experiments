from Environments.two_rooms import SimpleEnv
from minigrid.wrappers import FullyObsWrapper

import numpy as np
import imageio
env = SimpleEnv(render_mode = "rgb_array")

load_values = np.load('td_values_alpha_0.1.npy', allow_pickle=True).item()  


#tyo max entropy exploration ma chain, if q tables ko value around ma zero xa vane
# namrai kana explore ani sabai agree garepaxi exploit

frames = []
episodes = 1
rewards = []
for ep in range(episodes):
    done = False
    obs, info = env.reset()
    while not done:
        pos = env.agent_pos
        dir = env.agent_dir
        obs = (pos[0], pos[1], dir)
        q_values = [load_values.get((obs, a), 0) for a in range(3)]
        max_q = max(q_values)
        action = np.random.choice([a for a, q in enumerate(q_values) if q == max_q])
        next_obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        frame = env.render()
        frames.append(frame)
        if done:
            rewards.append(reward)
            break



imageio.mimsave('td_agent.gif', frames, fps=5, loop=0)
# print(f'Average reward over {episodes} episodes: {np.mean(rewards)}')
# # Number of solved episodes
# rewards = np.array(rewards)
# solved_episodes = np.sum(rewards > 0)
# print(solved_episodes)
