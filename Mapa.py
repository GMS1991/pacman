import pygame

class Mapa:
    
    #Constructor
    def __init__(self, mapa, panel):
        self.mapa = mapa
        self.panel = panel
        self.color_pared = (0, 0, 255)
        self.color_punto = (255, 255, 255)

    #dibujamos el mapa dinamicamente
    def draw(self, pantalla):
        for y, row in enumerate(self.mapa):
            for x, tile in enumerate(row):
                if tile == "#":
                    pygame.draw.rect(pantalla, self.color_pared,
                                     pygame.Rect(x * self.panel, y * self.panel, 
                                                 self.panel, self.panel))
                else:
                    pygame.draw.circle(pantalla, self.color_punto, 
                                       (x * self.panel + self.panel // 2,
                                        y * self.panel + self.panel // 2), 5)
