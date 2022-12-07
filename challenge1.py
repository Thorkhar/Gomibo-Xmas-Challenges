# Santa cardio

def parse(instr: str) -> int:
    floor = 0
    open_cnt = 0
    close_cnt = 0
    instr_array = list(instr)
    for i in instr_array:
        if i == "(":
            floor += 1
            open_cnt += 1
        if i == ")":
            floor -= 1
            close_cnt += 1
    
    print('Santa has ended at floor ' + str(floor) + ' by going up ' + str(open_cnt) + ' times and going down ' + str(close_cnt) + ' times')
    return [floor, open_cnt, close_cnt]

with open('input1.txt', 'r') as file:
    instructions = file.read()

parse(instructions)