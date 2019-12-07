from collections import defaultdict

def getPlanetsConnection():
    planets = defaultdict(list)
    with open('input') as f:
        for line in f:
            split = line.rstrip('\n').split(')')
            planets[split[0]].append(split[1])
    return planets 

def getToRoot(planets, planet, root='COM'):
    route = []
    looking = planet
    while looking != 'COM':
        for i in planets:
            if looking in planets[i]:
                route.append(i)
                looking = i
                break
    return route

def getMoving(planets, planet1, planet2):
    route1 = getToRoot(planets, planet1)
    route2 = getToRoot(planets, planet2)

    common = set(route1) & set(route2)
    sortedCommon = sorted(common, key=lambda x: len(getToRoot(planets, x)))
    maxLen = len(getToRoot(planets, sortedCommon[-1]))

    return (len(route1) - maxLen) + (len(route2) - maxLen) - 2

def countOrbits(planets, planet, count=0, total=0):
    total += count
    for satellite in planets[planet]:
        total = countOrbits(planets, satellite, count+1, total)
    return total


def main():
    planets = getPlanetsConnection()
    print("Part 1 :" + str(countOrbits(planets, 'COM')))
    print("Part 2: "+ str(getMoving(planets, "YOU", "SAN")))

if __name__ == "__main__":
    main()
