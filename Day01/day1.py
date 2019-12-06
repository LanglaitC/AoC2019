import json
import math

def calculateNeededFuel(data):
    somme = 0
    fuels = []
    for each in data:
        fuelToAdd = math.floor(each / 3) - 2
        fuels.append(fuelToAdd)
        somme += fuelToAdd if fuelToAdd > 0 else 0
    if somme:
        somme += calculateNeededFuel(fuels)
    return somme

## First version

# if __name__ == '__main__':
#     data = json.load(open('./data.json'))
#     somme = 0
#     for each in data:
#         somme += math.floor(each / 3) - 2
#     print(somme)

## Second version

if __name__ == '__main__':
    data = json.load(open('./data.json'))
    print(calculateNeededFuel(data))
