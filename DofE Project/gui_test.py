import pygame

class Window:
    def __init__(self):
        self.window = pygame.display
        self.window.set_mode((600,600))
        self.window.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 20)

    def update(self):
        while True:
            self.window.update()
            mouse_pos = pygame.mouse.get_pos()
            text = self.font.render(str(mouse_pos), False, (100, 20, 150))
            self.window.set_mode((600,600)).blit(text, (500,0))
            self.show_board()
    
    def show_board(self):
        pygame.draw.line(self.window.set_mode((600,600)), (35,200,35), (200,550), (200,50))
        pygame.draw.line(self.window.set_mode((600,600)), (35,200,35), (400,550), (400,50))


window = Window()
window.update()
