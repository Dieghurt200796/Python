from copy import deepcopy
import random

class Sudoku:
    def __init__(self):
        self.solution_number = 0

    @classmethod
    def read_puzzle(cls):
        path = "sudoku/puzzles.data"
        file = open(path, 'r')

        data = file.read().splitlines()

        return data

    def parse_puzzle_string(self, data):
        puzzles = []

        for sudoku in data:
            current_pos = 0
            previous_pos = 0
            digits = []
            for i in range(81):
                if (i + 1) % 9 == 0:
                    previous_pos = current_pos
                    current_pos = i + 1
                    digits.append(list(sudoku[previous_pos : current_pos]))
            puzzles.append(digits)

        self.puzzles = puzzles
    
    @classmethod
    def choose_puzzle(cls, index=None):
        lines = Sudoku.read_puzzle()
        if index is None:
            index = random.randrange(0, len(lines))
        sudoku = cls()
        sudoku.parse_puzzle_string(sudoku.read_puzzle())
        sudoku.puzzle = sudoku.puzzles[index]
        
        return sudoku

    def __repr__(self):
        styled_string = ""
        n = 1
        styled_string += ' ┏━━━━━┯━━━━━┯━━━━━┳━━━━━┯━━━━━┯━━━━━┳━━━━━┯━━━━━┯━━━━━┓\n'
        for row in deepcopy(self.puzzle):
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

    def check_positions(self, row, column, number):
        #Check if number can be placed in puzzle

        #Check row
        if str(number) in self.puzzle[row]:
            return False

        #Check column
        for i in range(9):
            if str(number) == self.puzzle[i][column]:
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
            section += self.puzzle[section_top + i][section_left : section_right]
        
        if str(number) in section:
            return False

        # Heuristic recursive backtracking algorithm
        # 1. Find an empty position
        # 2. Check numbers 1-10, find one that could fit.
        #       - Puzzle is completely filled, solved
        #       - A position with no possible numbers is found
        #           -> If so, remove the previous guess, start from step 1

        return True

    def solve(self):
        for row in range(9): #Find the next empty position
            for column in range(9):
                selected_number = self.puzzle[row][column]
                if selected_number == "0":
                    for n in range(1, 10): #Check numbers 1-9 to see if they fit
                        if self.check_positions(row, column, n):
                            self.puzzle[row][column] = str(n)

                            yield from self.solve()
                            
                            self.puzzle[row][column] = "0"
                    #If the for loop has ended, there was a mitake. No numbers 1-9 fit.
                    return
        self.solution_number += 1
        print(f"SOLUTION {self.solution_number}:\n", self, file=open("sudoku/puzzles_solved.info", "a", encoding="utf-8"), sep="")
        yield


if __name__ == "__main__":
    sudoku = Sudoku.choose_puzzle(0)
    print("PUZZLE:\n", sudoku, file=open("sudoku/puzzles_solved.info", "a", encoding="utf-8"), sep="")
    solver = sudoku.solve()
    for solution in solver:
        pass
