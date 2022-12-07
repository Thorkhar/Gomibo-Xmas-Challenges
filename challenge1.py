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
    return [floor, open_cnt, close_cnt]

with open('input1.txt', 'r') as file:
    instructions = file.read()

print(parse(instructions)[0])