import pygame
import sys
from Pacman import Pacman
from Mapa import Mapa

# Inicializar Pygame
pygame.init()

# Configurar la ventana del juego
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pacman")

# Disenio del mapa
TILE_SIZE = 40
# mapa = [
#     "####################",
#     "#........#.........#",
#     "#.####.#.#.#######.#",
#     "#........#.........#",
#     "####################"
# ]




mapa = [
    "####################",
    "#.....#######......#",
    "#..................#",
    "#.#####.#  #.#####.#",
    "#.......#  #.......#",
    "#.##.##.#  #.##.##.#",
    "#.......####.......#",
    "#.####........####.#"
    "#........##........#",
    "####################"
]


# Crear instancias de Pacman y Mapa
pacman = Pacman(1 * TILE_SIZE, 1 * TILE_SIZE, 5)
mapa_juego = Mapa(mapa, TILE_SIZE)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tecla = pygame.key.get_pressed()
    pacman.mover(tecla, mapa, TILE_SIZE)
    # Dibujar en la ventana del juego
    pantalla.fill((0, 0, 0))
    mapa_juego.draw(pantalla)
    pacman.dibujar(pantalla, TILE_SIZE)
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
