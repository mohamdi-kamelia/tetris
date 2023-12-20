import pygame
from menu import Menu 
from game import Game
import sys

pygame.init()
window = pygame.display.set_mode((400 ,650))
pygame.display.set_caption("Tetris")

game = Game()
def options():
    print("Options lancées.")

def quitter():
    pygame.quit()
    quit()

def main():
    menu = Menu(window)
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitter()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()
                
            option_selected = menu.handle_event(event)
            if option_selected:
                if option_selected == 1:
                    nouvelle_partie(menu , game)
                elif option_selected == 2:
                    options()
                elif option_selected == 3:
                    quitter()    

        window.fill((44, 44, 127))
        if menu.game_state == "menu":
            menu.draw()
        elif menu.game_state == "grid":
            #grid.draw(window)  # Dessine la grille
            game.draw(window)
       
        pygame.display.flip()
def nouvelle_partie(menu, grid ):
    menu.game_state = "grid"
    

if __name__ == "__main__":
    main()