def calVelocity(moons, lastVelocity=[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]):
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

def getStepsToRepeat(moons):
    velocity = [[[0,0,0], [0,0,0], [0,0,0], [0,0,0]]]
    moonPositions = [moons]
    i = 0
    while True:
        i += 1
        newVelocity = calVelocity(moonPositions[-1])
        velocity.append(newVelocity)
        newMoonPosition = getNewPostion(moonPositions[-1], velocity[-1])
        if newMoonPosition == moonPositions[0]:
            return i+1
        moonPositions.append(newMoonPosition)


def main():
    moons = [[14, 4, 5], [12,10,8], [1,7,-10], [16,-5,3]]
    moonPosition, velocity = simulateMoonPostions(moons)
    totalEnergy = calEnergy(moonPosition[-1],velocity[-1])
    print('Part 1: ',totalEnergy)
    print('Part 2: ',getStepsToRepeat(moons))
if __name__ == '__main__':
    main()
