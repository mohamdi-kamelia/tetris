
import pygame
from menu import Menu

pygame.init()
window = pygame.display.set_mode((400, 650))

def nouvelle_partie():#(on dois faire lo code de jeu là pour que quand on clique sur nouvelle partie il ouvre drctement le jeu)
    print("Nouvelle partie lancée.")

def options():
    print("Options lancées.")

def quitter():
    pygame.quit()
    quit()

def main():
    menu = Menu(window)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitter()

            option_selected = menu.handle_event(event)
            if option_selected:
                if option_selected == 1:
                    nouvelle_partie()
                elif option_selected == 2:
                    options()
                elif option_selected == 3:
                    quitter()

        menu.draw()
        pygame.display.flip()

if __name__ == "__main__":
    main()

