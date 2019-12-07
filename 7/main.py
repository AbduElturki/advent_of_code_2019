def getOpcode(intcode):
    opcode = intcode % 100
    operand1Mode = intcode // 100 % 10
    operand2Mode = intcode // 1000 % 10
    operand3Mode = intcode // 10000 % 10
    return opcode, [operand1Mode, operand2Mode, operand3Mode]

def runThrustProgram(ampInputs, feedback=False):
    with open('input') as f:
        intcode = f.readline().rstrip('\n').split(',')
    intcode = list(map(int, intcode))

    i = 0
    ampInputsIdx = 0
    while intcode[i] != 99:
        opcode, modes = getOpcode(intcode[i])
        if opcode == 1:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            intcode[intcode[i+3]] = operand1 + operand2
            i += 4
        elif opcode == 2:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            intcode[intcode[i+3]] = operand1 * operand2
            i += 4
        elif opcode == 3:
            intcode[intcode[i+1]] = ampInputs[ampInputsIdx]
            ampInputsIdx = (ampInputsIdx + 1) % len(ampInputs)
            i += 2
        elif opcode == 4:
            intcode[0] = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            i += 2
        elif opcode == 5:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            if operand1 != 0:
                i = operand2
            else:
                i += 3
        elif opcode == 6:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            if operand1 == 0:
                i = operand2
            else:
                i += 3
        elif opcode == 7:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            if operand1 < operand2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i += 4
        elif opcode == 8:
            operand1 = intcode[i+1] if modes[0] else intcode[intcode[i+1]]
            operand2 = intcode[i+2] if modes[1] else intcode[intcode[i+2]]
            if operand1 == operand2:
                intcode[intcode[i+3]] = 1
            else:
                intcode[intcode[i+3]] = 0
            i += 4
        else:
            print("I broke at index: " + str(i))
            break
        if ampInputsIdx % 2 and feedback:
            ampInput[ampInputsIdx] = intcode[0]
    return intcode[0]

def findHighestThrustFeedback():
    possibleInputs = []
    results = {}
    for i in range(5,10):
        for j in range(5,10):
            for k in range(5,10):
                for l in range(5,10):
                    for g in range(5,10):
                        a = [i,j,k,l,g]
                        if len(a) == len(set(a)):
                            a = [i,0,j,0,k,0,l,0,g,0]
                            possibleInputs.append(a)

def findHighestThrustLinear():
    possibleInputs = []
    results = {}
    for i in range(0,5):
        for j in range(0,5):
            for k in range(0,5):
                for l in range(0,5):
                    for g in range(0,5):
                        a = [i,j,k,l,g]
                        if len(a) == len(set(a)):
                            possibleInputs.append(a)
    for ampInput in possibleInputs:
        lastOutput = 0
        for i in ampInput:
            lastOutput = runThrustProgram([i,lastOutput])
        name = "".join(map(str,ampInput))
        results[name] = lastOutput
    maxInput = max(results, key=results.get)
    return results[maxInput]


def main():

    print(findHighestThrustLinear())

if __name__ == "__main__":
    main()
