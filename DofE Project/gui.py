import pygame, sys

class GUI:
    def __init__(self):
        self.black = (33, 36, 39)
        self.white = (246, 246, 246)
        self.red = (255, 0, 0)

        self.WIDTH = 100
        self.HEIGHT = 100
        self.MARGIN = 5

        self.moves = 0

        self.grid = []
        for row in range(3):
            self.grid.append([])
            for column in range(3):
                self.grid[row].append(0) 

        pygame.init()

        window_size = [self.WIDTH*3 + self.MARGIN*2, self.HEIGHT*3 + self.MARGIN*2]
        self.scr = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Tic Tac Toe Game")
        
        self.fontques = pygame.font.SysFont(None, 24)
        self.fontoption = pygame.font.SysFont(None, 22)
        
        self.row = None
        self.column = None

        self.cross = pygame.image.load('C:/Users/Dieghurt/OneDrive/Documents/GitHub/Python/Python/DofE Project/cross.png')
        self.cross = pygame.transform.scale(self.cross, [self.WIDTH,self.HEIGHT])
        self.circle = pygame.image.load('C:/Users/Dieghurt/OneDrive/Documents/GitHub/Python/Python/DofE Project/circle.png')
        self.circle = pygame.transform.scale(self.circle, [self.WIDTH,self.HEIGHT])

    def draw_intro(self):
        mode, difficulty, piece = 0,0,0
        
        while mode == 0:
            pos = pygame.mouse.get_pos()

            self.scr.fill((0,0,0))
            txt0 = self.fontques.render('Welcome. Choose gamemode:', True, self.white)
            
            if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                txt1 = self.fontoption.render('Friend', True, (65,65,65))
                pygame.draw.rect(self.scr,
                                (223, 230, 233),
                                [90,140,
                                125,
                                35])
            else:
                txt1 = self.fontoption.render('Friend', True, self.black)
                pygame.draw.rect(self.scr,
                                self.white,
                                [90,140,
                                125,
                                35])

            if pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                txt2 = self.fontoption.render('Bot', True, (65,65,65))
                
                pygame.draw.rect(self.scr,
                                (223, 230, 233),
                                [90,190,
                                125,
                                35])
            else:
                pygame.draw.rect(self.scr,
                                self.white,
                                [90,190,
                                125,
                                35])
                txt2 = self.fontoption.render('Bot', True, self.black)

            self.scr.blit(txt0, (40, 100))
            self.scr.blit(txt1, (127, 150))
            self.scr.blit(txt2, (137, 200))


            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                        mode = 1
                    elif pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                        mode = 2

            pygame.display.flip()

        if mode == 2:
            while difficulty == 0:
                pos = pygame.mouse.get_pos()

                self.scr.fill((0,0,0))
                txt0 = self.fontques.render('Now choose difficulty:', True, self.white)
                
                if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                    txt1 = self.fontoption.render('Easy', True, (65,65,65))
                    pygame.draw.rect(self.scr,
                                    (223, 230, 233),
                                    [90,140,
                                    125,
                                    35])
                else:
                    txt1 = self.fontoption.render('Easy', True, self.black)
                    pygame.draw.rect(self.scr,
                                    self.white,
                                    [90,140,
                                    125,
                                    35])

                if pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                    txt2 = self.fontoption.render('Hard', True, (65,65,65))
                    
                    pygame.draw.rect(self.scr,
                                    (223, 230, 233),
                                    [90,190,
                                    125,
                                    35])
                else:
                    pygame.draw.rect(self.scr,
                                    self.white,
                                    [90,190,
                                    125,
                                    35])
                    txt2 = self.fontoption.render('Hard', True, self.black)

                self.scr.blit(txt0, (65, 100))
                self.scr.blit(txt1, (134, 150))
                self.scr.blit(txt2, (134, 200))


                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit() 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                            difficulty = 1
                        elif pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                            difficulty = 2

                pygame.display.flip()

            while piece == 0:
                pos = pygame.mouse.get_pos()

                self.scr.fill((0,0,0))
                txt0 = self.fontques.render('Now choose your piece:', True, self.white)
                
                if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                    txt1 = self.fontoption.render('Crosses', True, (65,65,65))
                    pygame.draw.rect(self.scr,
                                    (223, 230, 233),
                                    [90,140,
                                    125,
                                    35])
                else:
                    txt1 = self.fontoption.render('Crosses', True, self.black)
                    pygame.draw.rect(self.scr,
                                    self.white,
                                    [90,140,
                                    125,
                                    35])

                if pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                    txt2 = self.fontoption.render('Circles', True, (65,65,65))
                    
                    pygame.draw.rect(self.scr,
                                    (223, 230, 233),
                                    [90,190,
                                    125,
                                    35])
                else:
                    pygame.draw.rect(self.scr,
                                    self.white,
                                    [90,190,
                                    125,
                                    35])
                    txt2 = self.fontoption.render('Circles', True, self.black)

                self.scr.blit(txt0, (65, 100))
                self.scr.blit(txt1, (125, 150))
                self.scr.blit(txt2, (127, 200))


                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        pygame.quit()
                        sys.exit() 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pos[0] > 90 and pos[0] < 215 and pos[1] < 175 and pos[1] > 140:
                            piece = 1
                        elif pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                            piece = 2

                pygame.display.flip()

        return mode, difficulty, piece

    def game_over(self, draw : bool, victor = ""):
        playagain = None
        if draw == True: txt0 = self.fontques.render('Draw.', True, self.white)
        else: txt0 = self.fontques.render(f'{victor} won.', True, self.white)
        while playagain == None:
            pos = pygame.mouse.get_pos()
            self.scr.fill((0,0,0))

            if pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                txt1 = self.fontoption.render('Ok', True, (65,65,65))
                
                pygame.draw.rect(self.scr,
                                (223, 230, 233),
                                [90,190,
                                125,
                                35])
            else:
                pygame.draw.rect(self.scr,
                                self.white,
                                [90,190,
                                125,
                                35])
                txt1 = self.fontoption.render('Ok', True, self.black)

            if draw: self.scr.blit(txt0, (130, 100))
            else: self.scr.blit(txt0, (100,100))
            self.scr.blit(txt1, (140, 200))
            

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 90 and pos[0] < 215 and pos[1] < 225 and pos[1] > 190:
                        pygame.quit()
                        exit()

            pygame.display.flip()

        return playagain


    def draw_screen(self):
        clock = pygame.time.Clock()
        self.scr.fill((0,0,0))
        for row in range(3):
            for column in range(3):
                color = self.white
                pygame.draw.rect(self.scr,
                                color,
                                [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                self.WIDTH,
                                self.HEIGHT])
                if self.grid[row][column] == (1,0):
                    self.scr.blit(self.cross, [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                    (self.MARGIN + self.HEIGHT) * row + self.MARGIN])
                elif self.grid[row][column] == (1,1):
                    self.scr.blit(self.circle, [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                    (self.MARGIN + self.HEIGHT) * row + self.MARGIN])
                    
            clock.tick(50)
            pygame.display.flip()