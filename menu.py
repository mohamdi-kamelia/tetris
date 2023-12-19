
import pygame
class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font("Christmas Cookies.woff", 36)  
        self.options = ["Nouvelle partie", "Options", "Quitter"]
        self.selected_option = 0
        self.game_state = "menu"  # Nouvel attribut pour suivre l'état du jeu
        # Chargement de fond
        self.background_image = pygame.image.load("fond.jpg")
        self.background_rect = self.background_image.get_rect()

        # Positionnement des boutons
        button_width = 200
        button_height = 50
        self.button_rects = [
            pygame.Rect((self.surface.get_width() - button_width) // 2, 200 + i * 70, button_width, button_height)
            for i in range(len(self.options))
        ]

    def draw(self):
        # Affichage de l'image de fond
        self.surface.blit(self.background_image, self.background_rect)

        for i, option in enumerate(self.options):
            # Choisissez la couleur en fonction de l'option
            if i == 0:  # Nouvelle partie
                color = (0, 200, 255)  # Bleu
            elif i == 1:
                color = (0 , 255, 0)
            else :
                color = (255, 0 , 0) 

            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.surface.get_width() // 2, 220 + i * 70))
            self.surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                mouse_x, mouse_y = event.pos
                for i, button_rect in enumerate(self.button_rects):
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        if i == 0:  # Si "Nouvelle partie" est cliqué
                            self.game_state = "grid"  # Change l'état du jeu vers la grille
                        return i + 1  # Les options commencent à 1 dans votre exemple
        return 0



