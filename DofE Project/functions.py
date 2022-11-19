import random, time
class Board:
    def __init__(self):
        self.board_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # Initialising the matrix for the logic of the board. A zero represents an empty cell, a 1 a cross (X), and a two a circle (O).
        self.number_of_turns = 0

    def matrix_formatter(self, x, y):
        """Formats the matrix so it is legible on the board"""
        value = self.board_matrix[x][y]
        if value == 0:
            return " "
        elif value == 1:
            return "X"
        else:
            return "O"

    def turn_user_input(self):
        """The user inputs their turn so that it can then be drawn"""
        turn_finalised = False
        while not turn_finalised:
            (x,y) = tuple((input()).split(","))
            x,y = int(x),int(y)
            if self.board_matrix[x][y] == 0:
                # If the cell is marked as empty, draw
                turn_finalised = True
            else:
                # If not, try again
                print("Invalid cell.")
        return x,y

    def set_cell(self, x, y):
        """The user's input is now added into self.board_matrix, ready to draw"""
        if self.number_of_turns % 2 == 0:
            self.board_matrix[x][y] = 1
            # If number of turns is even, it is X's turn, so draw cross
        else:
            self.board_matrix[x][y] = 2
            # If number of turns is not even, it is O's turn, so draw circle
        self.number_of_turns += 1
    
    def pick_pos_comp(self):
        position = None
        time.sleep(random.randint(1,3))
        while position != 0:
            x = random.randint(0,2)
            y = random.randint(0,2)
            position = self.board_matrix[x][y]
        return x,y	

    def show(self):
        """The board is drawn"""
        board = [[["   |", f" {self.matrix_formatter(0,0)} |", "___|"], ["   |", f" {self.matrix_formatter(1,0)} |", "___|"], ["   ", f" {self.matrix_formatter(2,0)} ", "___"]], 
                 [["   |", f" {self.matrix_formatter(0,1)} |", "___|"], ["   |", f" {self.matrix_formatter(1,1)} |", "___|"], ["   ", f" {self.matrix_formatter(2,1)} ", "___"]],
                 [["   |", f" {self.matrix_formatter(0,2)} |", "   |"], ["   |", f" {self.matrix_formatter(1,2)} |", "   |"], ["   ", f" {self.matrix_formatter(2,2)} ", "   "]]]
        board_to_print = ""
        for row in board:
            for i in range(3):
                for sections in range(len(row)):
                    board_to_print += row[sections][i]
                board_to_print += "\n"
        print(board_to_print)

    def check_for_victory(self):
        """This function checks for all the forms of winning the game. If the output is 0, nobody has won yet. If it is 1, crosses have won, and if it is 2, circles."""
        game_won_by = 0
        for i in range(3):
            for j in range(3):
                if self.board_matrix[i][j] != 0:
                    if j == 0:
                        if self.board_matrix[i][j] == self.board_matrix[i][j+1] and self.board_matrix[i][j] == self.board_matrix[i][j+2]:
                            game_won_by = self.board_matrix[i][j]
                            break
                    if i == 0:
                        if self.board_matrix[i][j] == self.board_matrix[i+1][j] and self.board_matrix[i][j] == self.board_matrix[i+2][j]:
                            game_won_by = self.board_matrix[i][j]
                            break
                        if j == 0 and self.board_matrix[i][j] == self.board_matrix[i+1][j+1] and self.board_matrix[i][j] == self.board_matrix[i+2][j+2]:
                            game_won_by = self.board_matrix[i][j]
                            break
                        if j == 2 and self.board_matrix[i][j] == self.board_matrix[i+1][j-1] and self.board_matrix[i][j] == self.board_matrix[i+2][j-2]:
                            game_won_by = self.board_matrix[i][j]
                            break
        return game_won_by
    
    def open_menu(self):
        self.mode = None
        self.piece = None
        while not self.mode:
            try:
                self.mode = int(input("Welcome to the game. Would you like to play 1.Against a friend or 2.Against the computer?\n"))
                if self.mode != 1 and self.mode != 2:
                    print("Invalid index")
                    self.mode = None

            except Exception as e:
                print(e, "\nTry again.")
        
        if self.mode == 2:
            while not self.piece:
                try:
                    self.piece = int(input("Would you like to play as 1.Crosses or 2.Circles?\n"))
                    if self.piece != 1 and self.piece != 2:
                        print("Invalid index")
                        self.piece = None
                except Exception as e:
                    print(e, "\nTry again.")

    def play_game(self):
        self.open_menu()
        if self.mode == 1:
            while True:
                self.show()
                victor = self.check_for_victory()
                if self.number_of_turns == 9:
                    print("Draw")
                    break
                if victor != 0:
                    if victor == 1: victor = "crosses"
                    else: victor = "circles"
                    print(f"Game won by: {victor}")
                    break
                x,y = self.turn_user_input()
                self.set_cell(x,y)
        elif self.mode == 2:
            while True:
                self.show()
                victor = self.check_for_victory()
                if self.number_of_turns == 9:
                    print("Draw")
                    break
                if victor != 0:
                    if victor == self.piece: victor = "player"
                    else: victor = "computer"
                    print(f"Game won by: {victor}")
                    break
                if (self.number_of_turns % 2) == 0:
                    # If number of turns is even, it is the turn of crosses. We will now check wheter or not the player picked to play as crosses.
                    if self.piece == 1: x,y = self.turn_user_input()
                    else: x,y = self.pick_pos_comp()

                if (self.number_of_turns % 2) == 1:
                    # If number of turns is odd, it is the turn of circles. We will now check wheter or not the player picked to play as circles.
                    if self.piece == 2: x,y = self.turn_user_input()
                    else: x,y = self.pick_pos_comp()
                self.set_cell(x,y)
