import pygame
import sys
from Pacman import Pacman
from Mapa import GameMap

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pacman")

# Disenio del mapa
TILE_SIZE = 40
map_data = [
    "####################",
    "#........#.........#",
    "#.####.#.#.#######.#",
    "#........#.........#",
    "####################"
]

# Crear instancias de Pacman y GameMap
pacman = Pacman(1 * TILE_SIZE, 1 * TILE_SIZE, 5)
game_map = GameMap(map_data, TILE_SIZE)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    pacman.move(keys, map_data, TILE_SIZE)

    # Dibujar en la ventana del juego
    screen.fill((0, 0, 0))
    game_map.draw(screen)
    pacman.draw(screen, TILE_SIZE)
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
