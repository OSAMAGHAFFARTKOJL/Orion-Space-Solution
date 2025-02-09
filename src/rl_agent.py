
from stable_baselines3 import PPO
import gym
import numpy as np

class SpaceEnv(gym.Env):
    def __init__(self):
        self.action_space = gym.spaces.Discrete(2)  # Start or Stop action
        self.observation_space = gym.spaces.Box(low=0, high=1, shape=(10,), dtype=np.float32)

    def step(self, action):
        reward = np.random.rand()
        return np.random.rand(10), reward, False, {}

    def reset(self):
        return np.random.rand(10)

env = SpaceEnv()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("models/rl_orion")
