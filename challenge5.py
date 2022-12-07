## Reindeer and presents

with open('input5.txt', 'r') as file:
    row_first = list(file.read())

def determine_rows(num_rows: int, first_row: list):
    num_houses = len(first_row)
    rows = [row_first]
    for row_num in range(1, num_rows): # Skip 1st row, already known
        new_row = []
        for house_nr in range(num_houses):
            prev_row = rows[row_num-1]
            if 0 < house_nr < num_houses-1:
                rlvnt_neighbours = [prev_row[house_nr-1], prev_row[house_nr], prev_row[house_nr+1]]
            elif house_nr == 0:
                rlvnt_neighbours = ['.', prev_row[house_nr], prev_row[house_nr+1]]
            elif house_nr == num_houses-1:
                rlvnt_neighbours = [prev_row[house_nr-1], prev_row[house_nr], '.']

            if is_naughty(rlvnt_neighbours) == True:
                new_row.append('^')
            else:
                new_row.append('.')
        rows.append(new_row)
    
    return rows

def is_naughty(nghbrs: list):
    if nghbrs[0] == '^' and nghbrs[1] == '^' and nghbrs[2] == '.':
        naughty = True
    elif nghbrs[0] == '.' and nghbrs[1] == '^' and nghbrs[2] == '^':
        naughty = True
    elif nghbrs[0] == '^' and nghbrs[1] == '.' and nghbrs[2] == '.':
        naughty = True
    elif nghbrs[0] == '.' and nghbrs[1] == '.' and nghbrs[2] == '^':
        naughty = True
    else:
        naughty = False
    
    return naughty

def houselist_to_str(houselist: list):
    house_str = ''
    for row in houselist:
        for house in row:
            house_str += house
        house_str += '\n'
    return house_str

def count_nice(num_rows, first_row):
    houselist = determine_rows(num_rows, first_row)
    houses = houselist_to_str(houselist)
    nice = houses.count('.')
    naughty = houses.count('^')
    total = len(first_row) * num_rows
    print('There are ' + str(nice) + ' nice houses, and ' + str(naughty) + ' naughty houses,')
    print('with a total of ' + str(nice + naughty) + ' houses, which should be equal to ' + str(total))
    
count_nice(40, row_first)