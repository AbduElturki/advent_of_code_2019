import re

def checkCondition(number):
    string = str(number)
    isAscending = lambda a: all(a[i] <= a[i+1] for i in range(len(a)-1))
    hasTwoAdjacents = lambda a: any(a[i] == a[i+1] or a[i] == a[i-1] \
                                    for i in range(1,(len(a) - 1)))
    return isAscending(string) and hasTwoAdjacents(string)

def checkConditionPart2(number):
    string = str(number)
    split = re.findall('(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)', string)

    isAscending = lambda a: all(a[i] <= a[i+1] for i in range(len(a)-1))
    anyPairs = lambda a: any(len(s) == 2 for s in a)

    return isAscending(string) and anyPairs(split) 

def main():
    inputRange = list(range(168630, 718098))
    meetCondition = list(map(checkCondition, inputRange))
    meetCondition2 = list(map(checkConditionPart2, inputRange))
    print("Part 1: " + str(sum(meetCondition)))
    print("Part 2: " + str(sum(meetCondition2)))

if __name__ == "__main__":
    main()
