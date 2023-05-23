import gym
import gym_examples
import time

env = gym.make(id="gym_examples/GridWorld-v0", render_mode='human')
obs = env.reset()

MAX_STEPS = 10
step = 0
done = False

while not done:
    print('step: ', step)

    act = env.action_space.sample()
    obs, reward, terminated, truncated,\
        info = env.step(act)

    done = True if terminated or truncated \
         or step >= MAX_STEPS else False
    
    env.render()
    time.sleep(0.5)
    step += 1

print('done with sim')
env.close()
