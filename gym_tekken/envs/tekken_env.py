import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np



class tekkenEnv(gym.env):
  """A tekken 7 environment for OpenAI gym"""
  metadata = {'render.modes': ['human']}
  
  def __init__(
               self
               game='tekken-7',
               mode='none',
               
                ):
    super(tekkenEnv, self).__init__()
    #define action and observation space
    #must be gym.spaces objects
    
    self.action_space=np.array([])
    
    self.observation_space=np.arrange()

  def step(self, action):
    #execute one step in the environment at a  time
    self._take_action()
    self.status = self.env.step()
    reward = self._get_reward()
    ob = self.env.getState()
    episode_over = self._reset(self)
    return ob, reward, episode_over, {}
 
  def reset(self):
    #reset environment to an initial state
  
  def render(self, mode='human', close =False):
    #render the environment to a screen
    pass
             
  def close(self):
     #close the environment
      
  def _get_reward(self):
    #define conditions needed to obtain reward signal
