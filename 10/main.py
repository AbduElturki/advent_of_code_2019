from math import gcd, pi, atan2

def findTheBestStation(asteriodMap):
    #(numOfSeen, X, R, setOfSeen)
    best = (0,0,0,set())
    xLen = len(asteriodMap[0])
    yLen = len(asteriodMap)
    for x1 in range(xLen):
        for y1 in range(yLen):
            if asteriodMap[y1][x1] != '#':
                continue
            slopes = set()
            for x2 in range(xLen):
                for y2 in range(yLen):
                    if asteriodMap[y2][x2] == '#' and (x2 != x1 or y2 != y1):
                        dx = x2 - x1
                        dy = y2 - y1
                        common = abs(gcd(dy,dx))
                        normalised = (dx//common , dy//common)
                        slopes.add(normalised)
            if len(slopes) > best[0]:
                best = (len(slopes),x1,y2,slopes)
    return best

def launchLaser(station):
    astroids = station[3]
    destroyedAstroids = []
    for (x, y) in astroids:
        astroidAngle = atan2(x,y)
        if astroidAngle > pi/2.0:
            astroidAngle -= 2*pi
        destroyedAstroids.append((astroidAngle, (x,y)))
    return list(reversed(sorted(destroyedAstroids)))

def main():
    lines = []
    for line in open('input').readlines():
        lines.append(line.strip())
    best = findTheBestStation(lines)
    print("Part 1 : the best station is at", \
            (best[1], best[2]), "with Line of Sight of", best[0], "asteroids")
    destroyedAstroids = launchLaser(best)

    dx, dy = destroyedAstroids[199][1]
    x, y = best[2]+dx, best[1]+dy
    while lines[x][y] != '#':
        x += dx
        y += dy

    print("Part 2:", y * 100 + x)

if __name__ == '__main__':
    main()
