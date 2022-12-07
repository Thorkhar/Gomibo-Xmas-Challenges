# Newspaper triangle puzzle

def validate_triangle(triangle: str) -> bool:
    side_lengths = list(triangle)
    for sd in range(len(side_lengths)):
        side_lengths[sd] = int(side_lengths[sd])
    valid = True
    if len(side_lengths) != 3:
        valid = False
        return valid

    if 0 in side_lengths:
        valid = False
        return valid

    for side_idx in range(len(side_lengths)):
        side_length = side_lengths[side_idx]
        leftover_sides = side_lengths.copy()
        leftover_sides.pop(side_idx)
        lftvr_side_sum = 0
        for lftvr_side in leftover_sides:
            lftvr_side_sum += lftvr_side

        if lftvr_side_sum <= side_length:
            valid = False
            break
    
    return valid

with open('input3.txt', 'r') as file:
    instructions = file.read().split()

def check_triangles(instructions:list) -> int:
    valid_cnt = 0
    false_cnt = 0
    total_triangles = len(instructions)
    for triangle in instructions:
        if validate_triangle(triangle) == True:
            valid_cnt += 1
        else:
            false_cnt += 1
    print('Valid: ' + str(valid_cnt))
    print('False: ' + str(false_cnt))
    print('Total triangles is ' + str(total_triangles) + ' while total parsed is ' + str(valid_cnt + false_cnt))
    return valid_cnt

check_triangles(instructions)