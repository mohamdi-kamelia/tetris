import pygame
from menu import Menu 
from game import Game
import sys

pygame.init()
window = pygame.display.set_mode((400 ,650))
pygame.display.set_caption("Tetris")

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

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
                pygame.quit()
                sys.exit()

            option_selected = menu.handle_event(event)
            if option_selected:
                if option_selected == 1:
                    nouvelle_partie(menu, Game)
                elif option_selected == 2:
                    options()
                elif option_selected == 3:
                    quitter()  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move_left()
                if event.key == pygame.K_RIGHT:
                    game.move_right()
                if event.key == pygame.K_DOWN:
                    game.move_down()  
                if event.key == pygame.K_UP:
                    game.rotate()      
            if event.type == GAME_UPDATE:
                game.move_down()     

        window.fill((44, 44, 127))
        if menu.game_state == "menu":
            menu.draw()
        elif menu.game_state == "grid":
            game.draw(window)  
            #game.move_down()  

        pygame.display.flip()
        
def nouvelle_partie(menu, grid ):
    menu.game_state = "grid"
    

if __name__ == "__main__":
    main()
