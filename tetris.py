import pygame
import sys
from grid import Grid

pygame.init()

dark_blue = (44, 44, 127)

window = pygame.display.set_mode((500 ,750))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(dark_blue)
    pygame.display.flip()
    clock.tick(60)

    # we will greate a grid class 





