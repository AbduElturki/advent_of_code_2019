def runGravityAssist(noun, verb):
    with open('input') as f:
        intcode = f.readline().rstrip('\n').split(',')
    intcode = list(map(int, intcode))
    intcode[1] = noun
    intcode[2] = verb 
    i = 0
    while intcode[i] != 99:
        if intcode[i] == 1:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] +\
                    intcode[intcode[i+2]]
        elif intcode[i] == 2:
            intcode[intcode[i+3]] = intcode[intcode[i+1]] *\
                    intcode[intcode[i+2]]
        else:
            print("I broke at index: " + str(i))
            break
        i += 4
    return intcode[0]

def findVerbAndNoun(output):
    result = 0
    for verb in range(99):
        for noun in range(99):
            result = runGravityAssist(noun, verb)
            if output == result:
                return (100 * noun + verb)
    print("Can't find it")
    return "error"

def main():
    print("Part one: " + str(runGravityAssist(12,2)))
    print("Part two: " + str(findVerbAndNoun(19690720)))

if __name__ == "__main__":
    main()
