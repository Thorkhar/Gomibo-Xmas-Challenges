keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def crack_codeline(instr: str, start_button = [1, 1]) -> int:
    button_coords = start_button
    instr_array = list(instr)
    for i in instr_array:
        current_row = button_coords[0]
        current_col = button_coords[1]
        if i == 'U':
            if 0 <= current_row - 1 <= 2:
                new_row = current_row - 1
            else:
                new_row = current_row
            new_col = current_col
        if i == 'D':
            if 0 <= current_row + 1 <= 2:
                new_row = current_row + 1
            else:
                new_row = current_row
            new_col = current_col
        if i == 'L':
            if 0 <= current_col - 1 <= 2:
                new_col = current_col - 1
            else:
                new_col = current_col
            new_row = current_row
        if i == 'R':
            if 0 <= current_col + 1 <= 2:
                new_col = current_col + 1
            else:
                new_col = current_col
            new_row = current_row
        
        button_coords = [new_row, new_col]
    return button_coords

def crack_code(instr_set: list, keypad: list):
    start_button = [1, 1]
    code_coords = []
    for row in instr_set:
        code_number = crack_codeline(row, start_button)
        code_coords.append(code_number)
        start_button = code_number
    print(code_coords)

    code = ''
    for num in code_coords:
        code += str(keypad[num[0]][num[1]])
        
    return code

with open('input2.txt', 'r') as file:
    instructions = file.read().split('\n')

print(crack_code(instructions, keypad))