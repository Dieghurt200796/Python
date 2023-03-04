import random, time, copy, pygame

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
        """The user inputs their choice so that it can then be drawn"""
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

    def set_cell(self, x, y, board):
        """The user's input is now added into self.board_matrix, ready to draw"""
        if self.number_of_turns % 2 == 0:
            board[x][y] = 1
            # If number of turns is even, it is X's turn, so draw cross
        else:
            board[x][y] = 2
            # If number of turns is not even, it is O's turn, so draw circle
        self.number_of_turns += 1
    
    def pick_pos_comp_random(self):
        position = None
        time.sleep(random.randint(1,3))
        while position != 0:
            x = random.randint(0,2)
            y = random.randint(0,2)
            position = self.board_matrix[x][y]
        return x,y
    
    @staticmethod
    def minimax(board, remaining_moves, current_player):
        # temp_board_matrix = copy.deepcopy(self.board_matrix)
        # last_move = move # Records the last move made to be able to undo it in future
        # self.set_cell(move[0],move[1],temp_board_matrix)
        # possible_moves = self.possible_moves(temp_board_matrix)
        # if piece_comp == 0:
        #     piece_comp = 2

        if current_player == 2: # Checking if current player is the computer
            best_move = [-1, -1, -1_000_000]
        else:
            best_move = [-1, -1, 1_000_000]

        if remaining_moves == 0:
            return [-1, -1, 0]
        elif Board.check_for_victory(board) == 1:
            [-1, -1, -1]
        elif Board.check_for_victory(board) == 2:
            [-1, -1, 1]

        for cell in Board.possible_moves(board):
            x = cell[0]
            y = cell[1]
            board[x][y] = current_player

            if current_player == 1:
                new_player = 2
            else:
                new_player = 1
                
            score = Board.minimax(board, remaining_moves-1, new_player)

            board[x][y] = 0
            score[0] = x
            score[1] = y
            if current_player == 2:
                if score[2] > best_move[2]:
                    best_move = score
            else:
                if score[2] < best_move[2]:
                    best_move = score
        return best_move
        
    def pick_pos_comp_backtrack(self):
        # best_weight = -1_000_000
        # best_move = None
        # x, y = None
        # possible_moves = Board.possible_moves(self.board_matrix)
        
        # for move in possible_moves:
        #     weight = self.minimax(move, ((self.piece + 1) % 2))
        #     if weight > best_weight:
        #         best_weight = weight
        #         best_move = move
        # return best_move
        
        time.sleep(random.randint(1,2))

        move = Board.minimax(self.board_matrix, 9-self.number_of_turns, 2)
        x,y = move[0],move[1]

        return x,y

    @staticmethod
    def possible_moves(board):
        moves = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == 0:
                    move = x,y
                    moves.append(move)
        return moves

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

    @staticmethod
    def check_for_victory(board):
        """This function checks for all the forms of winning the game. If the output is 0, nobody has won yet. If it is 1, crosses have won, and if it is 2, circles."""
        game_won_by = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] != 0:
                    if j == 0:
                        if board[i][j] == board[i][j+1] and board[i][j] == board[i][j+2]:
                            game_won_by = board[i][j]
                            break
                    if i == 0:
                        if board[i][j] == board[i+1][j] and board[i][j] == board[i+2][j]:
                            game_won_by = board[i][j]
                            break
                        if j == 0 and board[i][j] == board[i+1][j+1] and board[i][j] == board[i+2][j+2]:
                            game_won_by = board[i][j]
                            break
                        if j == 2 and board[i][j] == board[i+1][j-1] and board[i][j] == board[i+2][j-2]:
                            game_won_by = board[i][j]
                            break
        return game_won_by
    
    def open_menu(self):
        self.mode = None
        self.piece = None
        self.difficulty = None
        while not self.mode:
            try:
                self.mode = int(input("Welcome to the game. Would you like to play 1.Against a friend or 2.Against the computer?\n"))
                if self.mode != 1 and self.mode != 2:
                    print("Invalid index")
                    self.mode = None

            except Exception as e:
                print(e, "\nTry again.")
        
        if self.mode == 2:
            while not self.difficulty:
                try:
                    self.difficulty = int(input("Would you like to play on 1.Easy or 2.Hard mode?\n"))
                    if self.difficulty != 1 and self.difficulty != 2:
                        print("Invalid index")
                        self.difficulty = None
                except Exception as e:
                    print(e, "\nTry again")
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
                victor = Board.check_for_victory(self.board_matrix)
                if self.number_of_turns == 9:
                    print("Draw")
                    break
                if victor != 0:
                    if victor == 1: victor = "crosses"
                    else: victor = "circles"
                    print(f"Game won by: {victor}")
                    break
                x,y = self.turn_user_input()
                self.set_cell(x,y,board=self.board_matrix)
        elif self.mode == 2:
            while True:
                self.show()
                victor = Board.check_for_victory(self.board_matrix)
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
                    elif self.difficulty == 1: x,y = self.pick_pos_comp_random()
                    else: x,y = self.pick_pos_comp_backtrack()

                if (self.number_of_turns % 2) == 1:
                    # If number of turns is odd, it is the turn of circles. We will now check wheter or not the player picked to play as circles.
                    if self.piece == 2: x,y = self.turn_user_input()
                    elif self.difficulty == 1: x,y = self.pick_pos_comp_random()
                    else: x,y = self.pick_pos_comp_backtrack()
                self.set_cell(x,y,board=self.board_matrix)

class GUI:
    def __init__(self):
        window = pygame.display.set_mode((600,600))
        
