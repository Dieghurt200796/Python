from copy import deepcopy

def style(puzzle):
    styled_string = ""

    n = 1
    styled_string += ' ┏━━━━━┯━━━━━┯━━━━━┳━━━━━┯━━━━━┯━━━━━┳━━━━━┯━━━━━┯━━━━━┓\n'
    for row in deepcopy(puzzle):
        for i in range(9):
            if row[i] == '0':
                row[i] = ' '
            else:
                row[i] = str(row[i])
                
        for i in range(3): 
            if i != 0:
                styled_string += ' '
            styled_string += ' ┃  '
            styled_string += '  │  '.join(row[i * 3 : (i + 1) * 3])
        styled_string += '  ┃ '
        styled_string += '\n '
        if n % 3 != 0:
            styled_string += "┠─────┼─────┼─────╂─────┼─────┼─────╂─────┼─────┼─────┨\n"

        if n % 3 == 0:
            if n != 9:
                styled_string += '┣━━━━━┿━━━━━┿━━━━━╋━━━━━┿━━━━━┿━━━━━╋━━━━━┿━━━━━┿━━━━━┫\n'
            else:
                styled_string += '┗━━━━━┷━━━━━┷━━━━━┻━━━━━┷━━━━━┷━━━━━┻━━━━━┷━━━━━┷━━━━━┛\n'
        n += 1

    styled_string += '\n\n'

    return styled_string

def check_positions(puzzle, row, column, number):
    #Check if number can be placer in puzzle

    #Check row
    if str(number) in puzzle[row]:
        return False

    #Check column
    for i in range(9):
        if str(number) == puzzle[i][column]:
            return False

    #Check section
    section = []

    section_top = row
    while section_top % 3 != 0:
        section_top -= 1
    section_bottom = section_top + 3

    section_left = column
    while section_left % 3 != 0:
        section_left -= 1
    section_right = section_left + 3
    
    for i in range(3):
        section += puzzle[section_top + i][section_left : section_right]
    
    if str(number) in section:
        return False


    return True

def solve(puzzle):
    for row in range(9): #Find the next empty position
        for column in range(9):
            selected_number = puzzle[row][column]
            if selected_number == "0":
                for n in range(1, 10): #Check numbers 1-9 to see if they fit
                    if check_positions(puzzle, row, column, n):
                        puzzle[row][column] = str(n)

                        solve(puzzle)
                        
                        puzzle[row][column] = "0"
                #If the for loop has ended, there was a mitake. No numbers 1-9 fit.
                return
    print(style(puzzle))
    exit()

path = "sudoku/puzzles.data"
file = open(path, 'r')

data = file.read().splitlines()
int_data = []

for sudoku in data:
    current_pos = 0
    previous_pos = 0
    digits = []
    for i in range(81):
        if (i + 1) % 9 == 0:
            previous_pos = current_pos
            current_pos = i + 1
            digits.append(list(sudoku[previous_pos : current_pos]))
    int_data.append(digits)

copyof_int_data = deepcopy(int_data)
# pretty_puzzles = style(copyof_int_data)

for i in range(50):
    solve(int_data[i])
