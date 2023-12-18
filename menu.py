# menu.py

import pygame

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.Font(None, 36)
        self.options = ["Nouvelle partie", "Options", "Quitter"]
        self.selected_option = 0

    def draw(self):
        self.surface.fill((0, 0, 0))  # Fond noir
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(self.surface.get_width() // 2, 50 + i * 50))
            self.surface.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.selected_option + 1  # Les options commencent à 1 dans votre exemple
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                mouse_x, mouse_y = event.pos
                for i, option in enumerate(self.options):
                    text_rect = self.font.render(option, True, (0, 0, 0)).get_rect(center=(self.surface.get_width() // 2, 50 + i * 50))
                    if text_rect.collidepoint(mouse_x, mouse_y):
                        return i + 1  # Les options commencent à 1 dans votre exemple
        return 0


