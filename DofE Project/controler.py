import functions,gui,pygame,sys

class Controler:
    def __init__(self):
        self.logic = functions.Board()
        self.view = gui.GUI()

    def run(self):
        mode, difficulty, piece_ = self.view.draw_intro()
        self.logic.mode, self.logic.difficulty, self.logic.piece = mode, difficulty, piece_

        play = True

        while True:
            victor = self.logic.check_for_victory(self.logic.board_matrix)
            if victor != 0:
                    if victor == 1: victor = "Crosses"
                    else: victor = "Circles"
                    self.view.game_over(False,victor)
                    return play
            if self.view.moves == 9: 
                self.view.game_over(True)
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit() 
                
                if self.logic.mode == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        column = pos[0] // (self.view.WIDTH + self.view.MARGIN)
                        row = pos[1] // (self.view.HEIGHT + self.view.MARGIN)
                        piece = self.view.moves % 2
                        if piece == 0:
                            piece += 2
                        piece_for_logic = (piece + 1) % 2
                        if piece_for_logic == 0:
                            piece_for_logic += 2

                        if self.logic.matrix_formatter(row, column) == " ":
                            self.logic.turn_user_input(row, column)
                            self.view.grid[row][column] = (1, self.view.moves%2)
                            self.logic.board_matrix[row][column] = (piece_for_logic)
                            self.view.moves += 1
                            self.view.draw_screen()
                
                elif self.logic.mode == 2:
                    if (self.view.moves % 2 == 0 and self.logic.piece == 1) or (self.view.moves % 2 == 1 and self.logic.piece == 2):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            column = pos[0] // (self.view.WIDTH + self.view.MARGIN)
                            row = pos[1] // (self.view.HEIGHT + self.view.MARGIN)
                            piece = self.view.moves % 2
                            piece_for_logic = (piece + 1) % 2
                            if piece_for_logic == 0:
                                piece_for_logic += 2

                            if self.logic.matrix_formatter(row, column) == " ":
                                self.logic.turn_user_input(row, column)
                                self.view.grid[row][column] = (1, self.view.moves % 2)
                                self.logic.board_matrix[row][column] = (piece_for_logic)
                                self.view.moves += 1
                                self.logic.number_of_turns += 1
                                self.view.draw_screen()
                    else:
                        if self.logic.difficulty == 1:
                            row, column = self.logic.pick_pos_comp_random()
                        else:
                            row, column = self.logic.pick_pos_comp_backtrack()
                        piece = self.view.moves % 2
                        piece_for_logic = (piece + 1) % 2
                        if piece_for_logic == 0:
                            piece_for_logic += 2

                        self.view.grid[row][column] = (1, self.view.moves % 2)
                        self.logic.board_matrix[row][column] = (piece_for_logic)
                        self.view.moves += 1
                        self.logic.number_of_turns += 1
                        self.view.draw_screen()

