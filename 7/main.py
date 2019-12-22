import sys
sys.path.append('../intcodeMachine')

from intcodeMachine import intcodeMachine
from itertools import permutations

def findHighestThrust(start=0, end=5):
    results = {}
    allPhaseSettings = list(map(list, permutations(range(start,end))))
    for programInput in allPhaseSettings:
        lastOutput = 0
        for setting in programInput:
            machine = intcodeMachine('input', [setting, lastOutput])
            lastOutput = machine.run()
            del machine
        programInputStr = "".join(map(str,programInput))
        results[programInputStr] = lastOutput
    maxInput = max(results, key=results.get)
    return results[maxInput]

def findHighestFeedbackThrust(start=5,end=10):
    results = {}
    allPhaseSettings = list(map(list, permutations(range(start,end))))
    for programInput in allPhaseSettings:
        setting = programInput.copy()
        machines =  [intcodeMachine('input', [i]) for i in setting]
        lastOutput = 0
        while all(not machine.halt for machine in machines):
            for machine in machines:
                machine.addInput(lastOutput)
                outputTemp = machine.run()
                if not machine.halt:
                    lastOutput = outputTemp
        programInputStr = "".join(map(str,programInput))
        results[programInputStr] = lastOutput
    maxInput = max(results, key=results.get)
    return results[maxInput]


if __name__ == '__main__':
    print('Part 1:',findHighestThrust())
    print('Part 2:',findHighestFeedbackThrust())
