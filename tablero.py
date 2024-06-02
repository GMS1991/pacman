
import pygame
import sys

class Tablero:
    
    def __init__(self, ancho, alto):
        self.ancho          = ancho
        self.alto           = alto
        self.windows.height   = 800
        self.ventana.alto  = 600
        self.ventana        = None
        
    def initialize_pygame(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((self.venta.ancho , self.ventana.alto))
        pygame.display.set_caption("PACMAN")
    
    def draw_board(self):
        #guardamos las tuplas con los valores de los colores
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        #ciclo principal de juego y el ciclo termina hasta que el usuario cierre la ventana
        running = True
        while running:
            
            #itera todos los eventos ocurridos en el ciclo de vida de la ventana
            for event in pygame.event.get():
                #si el usuario cierra la venta se ejecuta el evento QUIT
                if event.type == pygame.QUIT:
                    running = False
                    
            #fondo lleno de blanco
            self.ventana.fill(WHITE)

            #dibujamos un tablero con color negro 
            pygame.draw.rect(self.ventana, BLACK, (50, 50, self.ventana.ancho - 100, self.ventana.alto - 100),5)

            pygame.display.update()

        # Quit pygame
        pygame.quit()
        sys.exit()