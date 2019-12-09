def getOpcode(intcode):
    opcode = intcode % 100
    operand1Mode = intcode // 100 % 10
    operand2Mode = intcode // 1000 % 10
    operand3Mode = intcode // 10000 % 10
    return opcode, [operand1Mode, operand2Mode, operand3Mode]

def runBOOST():
    with open('input') as f:
        intcode = f.readline().strip().split(',')
    intcode = list(map(int, intcode))
    intcode.extend([0] * 1000000)
    i = 0
    relativeBase = 0
    while intcode[i] != 99:
        opcode, modes = getOpcode(intcode[i])
        operand1 = intcode[i+1] if modes[0] == 1\
                    else intcode[intcode[i+1] + relativeBase] if modes[0] == 2\
                    else intcode[intcode[i+1]]
        operand2 = intcode[i+2] if modes[1] == 1\
                    else intcode[intcode[i+2] + relativeBase] if modes[1] == 2\
                    else intcode[intcode[i+2]]
        operand3Addr = i+3 if modes[2] == 1\
                        else intcode[i+3] + relativeBase if modes[2] == 2\
                        else intcode[i+3]
        if opcode == 1:
            intcode[operand3Addr] = operand1 + operand2 
            i += 4
        elif opcode == 2:
            intcode[operand3Addr] = operand1 * operand2 
            i += 4
        elif opcode == 3:
            userInput = input('BOOST Shell >> ')
            intcode[operand3Addr] = int(userInput)
            i += 2
        elif opcode == 4:
            intcode[0] = operand1 
            i += 2
        elif opcode == 5:
            if operand1 != 0:
                i = operand2
            else:
                i += 3
        elif opcode == 6:
            if operand1 == 0:
                i = operand2
            else:
                i += 3
        elif opcode == 7:
            if operand1 < operand2:
                intcode[operand3Addr] = 1
            else:
                intcode[operand3Addr] = 0
            i += 4
        elif opcode == 8:
            if operand1 == operand2:
                intcode[operand3Addr] = 1
            else:
                intcode[operand3Addr] = 0
            i += 4
        elif opcode == 9:
            relativeBase += operand1
            i += 2
        else:
            print("I broke at index: " + str(i))
            break
    print(intcode[0])


if __name__ == "__main__":
    runBOOST()
