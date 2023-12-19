import pygame
from menu import Menu 
from grid import Grid
import sys
from Blocks import *

pygame.init()
window = pygame.display.set_mode((400 ,650))
pygame.display.set_caption("Tetris")

#clock = pygame.time.Clock()

gime_grid = Grid()
block = SBlock()
gime_grid.print_grid()
def options():
    print("Options lancées.")

def quitter():
    pygame.quit()
    quit()

def main():
    menu = Menu(window)
    grid = Grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitter()

            option_selected = menu.handle_event(event)
            if option_selected:
                if option_selected == 1:
                    nouvelle_partie(menu, grid)
                elif option_selected == 2:
                    options()
                elif option_selected == 3:
                    quitter()    

        window.fill((44, 44, 127))
        if menu.game_state == "menu":
            menu.draw()
        elif menu.game_state == "grid":
            grid.draw(window)  # Dessine la grille
            block.draw(window)    

        pygame.display.flip()
        #clock.tick(60)
def nouvelle_partie(menu, grid ):
    menu.game_state = "grid"
    

if __name__ == "__main__":
    main()
    





