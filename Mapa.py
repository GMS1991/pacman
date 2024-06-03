import pygame

class GameMap:
    def __init__(self, map_data, tile_size):
        self.map_data = map_data
        self.tile_size = tile_size
        self.wall_color = (0, 0, 255)
        self.point_color = (255, 255, 255)

    def draw(self, screen):
        for y, row in enumerate(self.map_data):
            for x, tile in enumerate(row):
                if tile == "#":
                    pygame.draw.rect(screen, self.wall_color, pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))
                else:
                    pygame.draw.circle(screen, self.point_color, (x * self.tile_size + self.tile_size // 2, y * self.tile_size + self.tile_size // 2), 5)
