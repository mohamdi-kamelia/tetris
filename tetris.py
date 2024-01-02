import pygame
from game import Game
from menu import Menu
import sys
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 30)
score_surface = title_font.render("Score", True, Colors.modern_red)
next_surface = title_font.render("Next", True, Colors.purple)
game_over_surface = title_font.render("GAME OVER", True, Colors.modern_red)
score_rect = pygame.Rect(420, 55, 170, 60)
next_rect = pygame.Rect(420, 215, 170, 180)
return_to_menu_rect = pygame.Rect(420, 300, 170, 60)  # Ajout du bouton "Retour au menu"
window = pygame.display.set_mode((600, 680))
pygame.display.set_caption("Tetris")

game = Game()
menu = Menu(window)

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        option_selected = menu.handle_event(event)
        if option_selected:
            if option_selected == 1:
                game.game_over = False
                game.reset()
                menu.game_state = "grid"
            elif option_selected == 2:
                # Mettez ici le code pour gérer les options
                pass
            elif option_selected == 3:
                pygame.quit()
                sys.exit()

        # Gestion du clic sur le bouton "Retour au menu"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if return_to_menu_rect.collidepoint(event.pos):
                game.game_over = False
                game.reset()
                menu.game_state = "menu"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_RETURN and game.game_over == True:
                game.game_over = False
                game.reset()
                menu.game_state = "grid"

        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    score_value_surface = title_font.render(str(game.score), True, Colors.modern_violet)
    window.fill(Colors.dark_blue)
    window.blit(score_surface, (469, 20, 50, 50))
    window.blit(next_surface, (475, 180, 50, 50))
    if game.game_over == True:
        window.blit(game_over_surface, (420, 450, 50, 50))

    pygame.draw.rect(window, Colors.modern_light_blue, score_rect, 0, 10)
    window.blit(score_value_surface, score_value_surface.get_rect(centerx=score_rect.centerx,
                                                                   centery=score_rect.centery))
    pygame.draw.rect(window, Colors.modern_light_blue, next_rect, 0, 10)

    return_to_menu_rect = pygame.Rect(420, 500, 170, 60)
    # Dessin du bouton "Retour au menu"
    pygame.draw.rect(window, Colors.modern_light_blue, return_to_menu_rect, 0, 10)
    return_to_menu_text = title_font.render("Retour au menu", True, Colors.modern_red)
    window.blit(return_to_menu_text, return_to_menu_rect.move(10, 10))

    game.draw(window)
    if menu.game_state == "menu":
        menu.draw()

    pygame.display.update()
    
