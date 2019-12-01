def main():
    mass = [int(line.rstrip('\n')) for line in open("input")]
    totalFuel = getFuel(mass)
    totalFuelOfFuel = getFuelOfFuel(mass)
    print("Total fuel: " + str(totalFuel))
    print("Total fuel of fuel: " + str(totalFuelOfFuel))

def getFuel(mass):
    total = 0
    for i in mass:
        total = total + max((i // 3 - 2), 0)
    return total

def getFuelOfFuel(mass):
    total = 0
    for i in mass:
        j = i
        while j > 0:
            total = total + max((j // 3 - 2), 0)
            j = max((j // 3 - 2), 0)
    return total


if __name__ == '__main__':
    main()
