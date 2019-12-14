import sys
sys.path.append('../intcodeMachine')

from intcodeMachine import intcodeMachine

def coloredTile(tile):
    if tile == 1:
        return '\033[91m1\033[0m'
    elif tile == 2:
        return '\033[93m2\033[0m'
    elif tile == 3:
        return '\033[94m-\033[0m'
    elif tile == 4:
        return '\033[92mO\033[0m'
    elif tile == 0:
        return " "
    else:
        return str(tile)

def countBlockTiles():
    tiles = [[0 for _ in range(37)] for _ in range(50)]
    system = intcodeMachine('input')
    while True:
        x = system.run()
        y = system.run()
        tile = system.run()
        if x == None or y == None or tile == None:
            break
        tiles[y][x] = tile
    numOfBlocks = 0
    for i in range(50):
        numOfBlocks += tiles[i].count(2)
    return numOfBlocks


def runArcadeAi():
    highscore = 0
    tiles = [[0 for _ in range(37)] for _ in range(50)]
    def aiPong():
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                if tiles[y][x] == 4:
                    print(x,y)
                    ballLoc = x
                if tiles[y][x] == 3:
                    padLoc = x
        if ballLoc > padLoc:
            return 1
        elif ballLoc < padLoc:
            return -1
        else:
            return 0
    system = intcodeMachine('input', aiPong)
    system.intcode[0] = 2
    while True:
        x = system.run()
        y = system.run()
        if x == -1 and y == 0:
            highscore = system.run()
            print(highscore)
            ai = True
        else:
            tile = system.run()
        if x == None or y == None or tile == None:
           break
        tiles[y][x] = tile
        for i in range(50):
            print(*list(map(coloredTile, tiles[i])))
        print('-' * 37)
        print('Score: ', highscore)
        print('-' * 37)
    return highscore

def runArcade():
    tiles = [[0 for _ in range(37)] for _ in range(50)]
    system = intcodeMachine('input')
    system.intcode[0] = 2
    while True:
        x = system.run()
        y = system.run()
        if x == -1 and y == 0:
            highscore = system.run()
            print(highscore)
        else:
            tile = system.run()
        if x == None or y == None or tile == None:
           break
        tiles[y][x] = tile
        for i in range(50):
            print(*list(map(coloredTile, tiles[i])))
        print('-------------------------------------')

if __name__ == '__main__':
    highscore = runArcadeAi()
    print('Part 1:', countBlockTiles())
    print('PArt 2:', highscore)
