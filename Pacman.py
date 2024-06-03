import pygame

class Pacman:
    
    
    #Constructor clase
    def __init__(self, x, y, velocidad):
        self.x = x
        self.y = y
        self.speed = velocidad
        self.color = (255, 255, 0)
        self.tamanio_celda = 1

    #Movimientos
    def mover(self, keys, mapa, panel):
        new_x, new_y = self.x, self.y
        #Aumentamos de 5 en 5 cada vez que seleccionamos una de las teclas
        if keys[pygame.K_LEFT]:
            new_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed
        
        #Validamos el movimiento    
        if self.valida_movimiento(new_x, new_y, mapa, panel):
            self.x, self.y = new_x, new_y
        
      
    #Validamos el movimiento
    # def valida_movimiento(self, x, y, mapa, panel):
    #     #x es el nuevo valor que se asiganra pero se divide por el tamanio del panel
    #     col = x // panel
    #     #y es el nuevo valor que se asiganra pero se divide por el tamanio del panel
    #     row = y // panel
    #     if mapa[row][col] == "#":
    #         return False

    def valida_movimiento(self, x, y, mapa, tile_size):
        # Convertir coordenadas de píxeles a coordenadas de la cuadrícula
        col = x // tile_size
        row = y // tile_size
        
        # Verificar límites del mapa
        if row < 0 or row >= len(mapa) or col < 0 or col >= len(mapa[0]):
            return False
        
        # Verificar si la nueva posición es una pared
        if mapa[row][col] == "#":
            return False
        
        return True
    
  
    
    def dibujar(self, pantalla, tamanio_celda):
        pygame.draw.circle(pantalla, self.color, (self.x + tamanio_celda // 2, self.y + tamanio_celda // 2), tamanio_celda // 2 - 5)
