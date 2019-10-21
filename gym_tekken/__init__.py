from gym.envs.registration import register

register(id='Tekken-v0',
         entry_point='gym_tekken.envs:TekkenEnv',
        )
