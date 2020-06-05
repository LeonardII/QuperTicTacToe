import numpy as np
import random
player = 1
#params
alpha = 0.1
gamma = 0.6
epsilon = 0.1

games2Train = 999999

env = [0,0,0,0,0,0,0,0,0]
qTable = np.zeros([19683,9])
rTable = []


def runTheGame():
    env = [0,0,0,0,0,0,0,0,0,0]
    while True:
        enemy = ai_move(env,99999)
        print(f"Enemy: I GO TO {enemy}")
        env[enemy] = 1
        for x in range(3):
            print(f'{env[x*3]} {env[x*3+1]} {env[x*3+2]}\n')
        fucku = int(input("Where do you go looser? "))
        env[fucku] = 2
        if getWin(env, 1):
            print("1 won")
        if getWin(env, 2):
            print("2 won")



def getNextState(array,a):
    if array[a] != 0:
        return getState(array) 
    array[a] = player
    return getState(array)

def step(action):
    if env[action] == 0:
        env[action] = player
    id = getState(env)
    okList = []
    for i in range(9):
        if env[i] == 0:
            okList.append(i)
    if(len(okList)==0):
        return getState(env),rTable[id][action][2],True
    env[random.choice(okList)] = (player - 3) * -1
    return getState(env),rTable[id][action][2],rTable[id][action][3]

    
def getEnv(n):
    a =  np.base_repr(n,base = 3)
    array = []
    string = str(a)
    for i in range(9-len(string)):
        array.append(0)
    for c in string:
        array.append(int(c))

    return array
        

def getState(array):
    state = 0
    for x in range(9):
        pp = pow(3,8-x)
        state += array[x] * pp
    return state

def ai_train():
    pass


def getWin(array,player):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if array[row[0]] == array[row[1]] == array[row[2]]:
            if array[row[0]] == player:
                return True


def ai_move(array,player):
    return np.argmax(qTable[getState(array)])



#SETUP rTable
for i in range(19683):
    array = getEnv(i)
    aList = []
    for x in range(9):
        reward = -1
        if array[x] != 0:
            reward = -10
        else:
            array[x] = player
            if getWin(array, player):
                reward = 20
        aList.append([1,getState(array),reward,reward > 0])
    rTable.append(aList)

#START
for i in range(1, games2Train):
    env = [0,0,0,0,0,0,0,0,0]
    state = 0
    epochs, penalties, reward = 0,0,0
    done = False

    while not done:
        if random.uniform(0,1) < epsilon:
            action = random.randint(0,8)
        else:
            action = np.argmax(qTable[state])
        next_state,reward,done = step(action)

        oldValue = qTable[state,action]
        nextMax = np.max(qTable[next_state])
        newValue = (1 - alpha) * oldValue + alpha * (reward + gamma * nextMax)

        qTable[state,action] = newValue

        if reward == -10:
            penalties += 1
        
        state = next_state
        epochs += 1

    if(i % 929 == 0):
        print(f'Loading: {round(i/games2Train * 100,2)}%')

while True:
    print("I WANT TO PLAY A GAME")
    i = input("ARE U READY MOTHERFUCKER? ")
    if i == 'y':
        runTheGame()
