code = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0]

def executeCode(code):
    position = 0
    while (code[position] != 99):
        if code[position] == 1:
            result = code[code[position + 1]] + code[code[position + 2]]
        elif code[position] == 2:
            result = code[code[position + 1]] * code[code[position + 2]]
        else:
            raise Exception("Oops, opcode is invalid, something went wrong")
        code[code[position + 3]] = result
        position += 4
    return code[0]

## version 1

# if __name__ == '__main__':
#     print(executeCode(code))

## version 2

if __name__ == '__main__':
    for noun in range(1, 99):
        for verb in range(1, 99):
            newCode = code[:]
            newCode[1] = noun
            newCode[2] = verb
            result = executeCode(newCode)
            if result == 19690720:
                print(noun * 100 + verb)