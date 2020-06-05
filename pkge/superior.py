import numpy as np
import random

#params
alpha = 0.1
gamma = 0.6
epsilon = 0.1

env = [2,2,2,2,2,2,2,2,2]
qTable = np.zeros([19683,9])

for i in range(1, 99999):
    state = 0
    epochs, penalties, reward = 0,0,0
    done = False

    while not done:
        if random.uniform(0,1) < epsilon:
            action = random.randint(0,8)
        else:
            action = np.argmax(qTable[state])
        next_state,reward,done,info = step(action)



def step(action):
    

def getState(env):
    state = 0
    for x in range(9):
        pp = pow(3,8-x)
        state += env[x] * pp

    return state

def ai_train():
    pass


def ai_move(board,player):
    return 1

print(getState())