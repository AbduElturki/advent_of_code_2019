from copy import deepcopy
from math import gcd

def calVelocity(moons, lastVelocity=[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]):
    #Shallow copy for reusue
    returnVal = lastVelocity.copy()
    for i, moon in enumerate(moons):
        for j, moonToCompare in enumerate(moons):
            if i == j:
                continue
            else:
                for k in range(3):
                    if moon[k] < moonToCompare[k]:
                        returnVal[i][k] += 1
                    elif moon[k] > moonToCompare[k]:
                        returnVal[i][k] -= 1
    return returnVal

def getNewPostion(moons, velocity):
    returnVal = []
    for i in range(4):
        tmp = []
        for k in range(3):
            tmpVal = moons[i][k] + velocity[i][k]
            tmp.append(tmpVal)
        returnVal.append(tmp)
    return returnVal

def calEnergy(moonLocations, velocity):
    pots = list(map(sum, [map(abs, x) for x in moonLocations]))
    kins = list(map(sum, [map(abs, x) for x in velocity]))
    return sum([p*k for p,k in zip(pots,kins)])

def simulateMoonPostions(moons, stop=1000):
    velocity = [[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]]
    moonPositions = [moons]
    for i in range(stop):
        newVelocity = calVelocity(moonPositions[-1])
        velocity.append(newVelocity)
        newMoonPosition = getNewPostion(moonPositions[-1], velocity[-1])
        moonPositions.append(newMoonPosition)
    return moonPositions, velocity

def calVelocity1D(moons, lastVelocity):
    returnVal = deepcopy(lastVelocity)
    for i, moon in enumerate(moons):
        for j, moonToCompare in enumerate(moons):
            if i == j: continue
            else:
                if moon < moonToCompare:
                    returnVal[i] += 1
                elif moon > moonToCompare:
                    returnVal[i] -=1
    return returnVal

def getNewPostion1D(moons, velocity):
    returnVal = []
    for i in range(len(moons)):
        returnVal.append(moons[i] + velocity[i])
    return returnVal

def getOrbit1D(moons, axis):
    velocity = [[0,0,0,0]]
    moonPos = [[moon[axis] for moon in moons]]
    steps = 0
    repeatFound = False
    while not repeatFound:
        steps += 1
        velocity.append(calVelocity1D(moonPos[-1], velocity[-1]))
        moonPos.append(getNewPostion1D(moonPos[-1], velocity[-1]))
        if moonPos[-1] == moonPos[0] and velocity[-1] == velocity[0]:
            repeatFound = True
    return steps

def getCompleteCycleSteps(moons):
    lcm = lambda x, y: x*y // gcd(x,y)
    xRepeats = getOrbit1D(deepcopy(moons), 0)
    yRepeats = getOrbit1D(deepcopy(moons), 1)
    zRepeats = getOrbit1D(deepcopy(moons), 2)
    return lcm(xRepeats,lcm(yRepeats, zRepeats))

def main():
    moons = [[14, 4, 5], [12,10,8], [1,7,-10], [16,-5,3]]
    moonPosition, velocity = simulateMoonPostions(moons)
    totalEnergy = calEnergy(moonPosition[-1],velocity[-1])
    print('Part 1: ',totalEnergy)
    moons = [[14, 4, 5], [12,10,8], [1,7,-10], [16,-5,3]]
    print('Part 2: ', getCompleteCycleSteps(moons))

if __name__ == '__main__':
    main()
