import pygame

class Pacman:
    
    
    #Constructor clase
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = (255, 255, 0)
        self.size = 20

    #Movimientos
    def move(self, keys, map_data, tile_size):
        new_x, new_y = self.x, self.y
        
       
        
        if keys[pygame.K_LEFT]:
            news_x -= self.speed
        if keys[pygame.K_RIGHT]:
            new_x += self.speed
        if keys[pygame.K_UP]:
            new_y -= self.speed
        if keys[pygame.K_DOWN]:
            new_y += self.speed
            
        if self.is_valid_move(new_x, new_y, map_data, tile_size):
            self.x, self.y = new_x, new_y
        
      

    def is_valid_move(self, x, y, map_data, tile_size):
        col = x // tile_size
        row = y // tile_size
        if map_data[row][col] == "#":
            return False
        return True

    def draw(self, screen, tile_size):
        pygame.draw.circle(screen, self.color, (self.x + tile_size // 2, self.y + tile_size // 2), tile_size // 2 - 5)
