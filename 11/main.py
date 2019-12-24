import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
sys.path.append('../intcodeMachine')

from intcodeMachine import intcodeMachine
from copy import deepcopy
from collections import defaultdict

def runPaintPanelProgram(initColor=0):
    panels = defaultdict(int)
    x = y = 0

    directionX = [0,1,0,-1]
    directionY = [-1,0,1,0]
    dirIdx = 0

    panels[(x,y)] = initColor

    def getColour():
        return panels[(x,y)]

    machine = intcodeMachine('input', getColour)

    while not machine.halt:
        colour = machine.run()
        if machine.halt:
            break
        panels[(x,y)] = colour
        turn = machine.run()
        if turn == 0:
            dirIdx = (dirIdx - 1) % 4
        else:
            dirIdx = (dirIdx + 1) % 4
        y += directionY[dirIdx]
        x += directionX[dirIdx]
    return panels

def getRegistration():
    panels = runPaintPanelProgram(1)
    xMax = max(panels.keys(), key=lambda x: x[0])[0] + 1
    yMax = max(panels.keys(), key=lambda x: x[1])[1] + 1
    reg = [[0]*xMax for _ in range(yMax)]
    regTerm = [[' ']*xMax for _ in range(yMax)]
    for row in range(yMax):
        for col in range(xMax):
            if panels[(col, row)] == 1:
                reg[row][col] = 255
                regTerm[row][col] ='*'
    plt.imshow(np.array(reg).reshape(yMax,xMax), cmap=cm.gray)
    plt.show()
    return regTerm


def main():
    print('Part 1:', len(runPaintPanelProgram()))
    resultToPrint =  getRegistration()
    print('Part 2:')
    for row in resultToPrint:
        print(*row,sep='')

if __name__ == '__main__':
    main()


