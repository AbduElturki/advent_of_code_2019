class intcodeMachine:
    def __init__(self,intcodeFile,inputs=[]):
        self.pc = 0
        self.rb = 0
        self.intcodeFile = intcodeFile
        self.intcode = list(map(int,
                                open(intcodeFile).read().strip().split(',')))
        self.intcode.extend([0] * 1000000)
        self.modes = [0,0,0]
        self.inputs = inputs

    def parseOpcode(self,intcode):
        opcode = intcode % 100
        operand1Mode = intcode // 100 % 10
        operand2Mode = intcode // 1000 % 10
        operand3Mode = intcode // 10000 % 10
        self.modes = [operand1Mode, operand2Mode, operand3Mode]
        return opcode

    def reset(self):
        self.pc = 0
        self.rb = 0
        self.intcode = list(map(int,
                                open(self.intcodeFile).read().strip().split(',')))
        self.intcode.extend([0] * 1000000)

    def addInput(self, newAddition):
        self.inputs.append(newAddition)

    def run(self):
        while self.intcode[self.pc] != 99:
            opcode = self.parseOpcode(self.intcode[self.pc])
            operand1 = self.intcode[self.pc+1] if self.modes[0] == 1\
                        else self.intcode[self.intcode[self.pc+1] + self.rb] if self.modes[0] == 2\
                        else self.intcode[self.intcode[self.pc+1]]
            operand2 = self.intcode[self.pc+2] if self.modes[1] == 1\
                        else self.intcode[self.intcode[self.pc+2] + self.rb] if self.modes[1] == 2\
                        else self.intcode[self.intcode[self.pc+2]]
            operand3Addr = self.pc+3 if self.modes[2] == 1\
                            else self.intcode[self.pc+3] + self.rb if self.modes[2] == 2\
                            else self.intcode[self.pc+3]
            if opcode == 1:
                self.intcode[operand3Addr] = operand1 + operand2
                self.pc += 4
            elif opcode == 2:
                self.intcode[operand3Addr] = operand1 * operand2
                self.pc += 4
            elif opcode == 3:
                if len(self.inputs) == 0:
                    userInput = input('IntcodeMachine Shell >> ')
                    self.intcode[operand3Addr] = int(userInput)
                elif type(self.inputs) == list:
                    self.intcode[operand3Addr] = self.inputs.pop(0)
                else:
                    self.intcode[operand3Addr] = self.inputs.pop(0)
                self.pc += 2
            elif opcode == 4:
                self.intcode[0] = operand1
                self.pc += 2
                return operand1
            elif opcode == 5:
                if operand1 != 0:
                    self.pc = operand2
                else:
                    self.pc += 3
            elif opcode == 6:
                if operand1 == 0:
                    self.pc = operand2
                else:
                    self.pc += 3
            elif opcode == 7:
                if operand1 < operand2:
                    self.intcode[operand3Addr] = 1
                else:
                    self.intcode[operand3Addr] = 0
                self.pc += 4
            elif opcode == 8:
                if operand1 == operand2:
                    self.intcode[operand3Addr] = 1
                else:
                    self.intcode[operand3Addr] = 0
                self.pc += 4
            elif opcode == 9:
                self.rb += operand1
                self.pc += 2
            else:
                print("I broke at index: " + str(self.pc))
                break

