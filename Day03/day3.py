import json
import math

data = json.load(open('./data.json'))

directions = {
    'U': (lambda x: tuple([x[0], x[1] + 1])),
    'D': (lambda x: tuple([x[0], x[1] - 1])),
    'R': (lambda x: tuple([x[0] + 1, x[1]])),
    'L': (lambda x: tuple([x[0] - 1, x[1]]))
}

def getPaths(stepsInfo):
    paths = []
    for index, each in enumerate(data):
        position = (0, 0)
        paths.append([position])
        stepsNumber = 0
        for move in each:
            direction = move[0]
            steps = int(move[1:])
            for _ in range(steps):
                stepsNumber += 1
                position = directions[direction](position)
                paths[index].append(position)
                stepsKey = tuple([index, position])
                if stepsKey not in stepsInfo:
                    stepsInfo[stepsKey] = stepsNumber
    return paths

def getClosestIntersection(paths):
    closest = None
    intersections = set(paths[0]) & set(paths[1])
    for _, each in enumerate(intersections):
        if each in paths[1]:
            manhattan = int(math.fabs(each[0]) + math.fabs(each[1]))
            if (closest is None or manhattan < closest) and manhattan > 0:
                closest = manhattan
    return closest

def getLessStepIntersection(paths, stepsInfo):
    lowest = None
    intersections = set(paths[0]) & set(paths[1])
    intersections.remove((0, 0))
    for each in intersections:
        print(stepsInfo[(0, each)], stepsInfo[(1, each)])
        steps = stepsInfo[(0, each)] + stepsInfo[(1, each)]
        if lowest is None or steps < lowest:
            lowest = steps
    return lowest

if __name__ == '__main__':
    steps = {}
    paths = getPaths(steps)
    print(getClosestIntersection(paths))
    print(getLessStepIntersection(paths, steps))