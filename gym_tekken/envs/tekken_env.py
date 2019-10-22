import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from PIL import ImageGrab
imprt cv2
import time

LastTime=time.time()
while(True):
  scrn= np.array(ImageGrab.grab(bbox=(0,40, 800, 640)))
  
  print('loop took {} seconds'.format(time.time()-LastTime))
  LastTime=time.time()
  cv2.imshow('window', cv2.cvtColor(scrn , cv2.COLOR_BGR2RGB)
  if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break

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
