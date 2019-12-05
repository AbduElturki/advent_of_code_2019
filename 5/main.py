def getOpcode(intcode):
    opcode = intcode % 100
    operand1Mode = intcode // 100 % 10
    operand2Mode = intcode // 1000 % 10
    operand3Mode = intcode // 10000 % 10
    return opcode, [operand1Mode, operand2Mode, operand3Mode]

def runDiagnosticProgram():
    with open('input') as f:
        intcode = f.readline().rstrip('\n').split(',')
    intcode = list(map(int, intcode))

    i = 0
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
            print("Please input the ID")
            userInput = input()
            intcode[intcode[i+1]] = int(userInput)
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
    print(intcode[0])

def main():
    runDiagnosticProgram()

if __name__ == "__main__":
    main()
