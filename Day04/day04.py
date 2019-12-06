lowest = 246515
highest = 739105

def isSixDigit(x):
    return len(str(x)) == 6

def gotTwoAdjacentSame(x):
    stringNumber = str(x)
    last = None
    for letter in stringNumber:
        if letter == last:
            return True
        last = letter
    return False

def gotOnlyTwoAdjacentSame(x):
    stringNumber = str(x)
    i = 0
    while (i < len(stringNumber)):
        j = i
        while(j < len(stringNumber) and stringNumber[j] == stringNumber[i]):
            j += 1
        if j - i == 2:
            return True
        i = j
    return False

def numberAreNotDecreasing(x):
    stringNumber = str(x)
    last = 0
    for letter in stringNumber:
        number = int(letter)
        if number < last:
            return False
        last = number
    return True

def firstVersion():
    matchingConditions = 0
    for each in range(lowest, highest):
        if (
            isSixDigit(each)
            and gotTwoAdjacentSame(each)
            and numberAreNotDecreasing(each)
        ):
            matchingConditions += 1
    return matchingConditions

def secondVersion():
    matchingConditions = 0
    for each in range(lowest, highest):
        if (
            isSixDigit(each)
            and gotOnlyTwoAdjacentSame(each)
            and numberAreNotDecreasing(each)
        ):
            matchingConditions += 1
    return matchingConditions

if __name__ == '__main__':
    print(firstVersion())
    print(secondVersion())