import gym
from gym import error, spaces, utils
from gym.utils import seeding

class tekkenEnv(gym.env):
  """A tekken 7 environment for OpenAI gym"""
  metadata = {'render.modes': ['human']}
  
  def __init__(self):
    super(tekkenEnv, self).__init__()
    #define action and observation space
    #must be gym.spaces objects

  def step(self, action):
    #execute one step in the environment at a  time
 
  def reset(self):
    #reset environment to an initial state
  
  def render(self, mode='human', close =False):
    #render the environment to a screen
