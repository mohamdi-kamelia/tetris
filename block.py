import pygame
from colors import colors

class Block:
    def __init__(self, block_id):  
        self.cell_size = 31
        self.rotation_state = 0
        self.colors = colors.get_cell_colors()

        # Assurez-vous que self.block_id est un index valide pour self.colors
        if block_id < 0 or block_id >= len(self.colors):
            # Si ce n'est pas le cas, définissez-le sur une valeur par défaut
            self.block_id = 0  # Vous pouvez choisir une valeur par défaut appropriée
        else:
            self.block_id = block_id

        # Supposons que self.cells est initialisé correctement ailleurs dans votre code
        self.cells = {}  

    def draw(self, window):
        tiles = self.cells.get(self.rotation_state, [])  # Utilisez get pour éviter une clé manquante
        for tile in tiles:
            tile_rect = pygame.Rect(
                tile.column * self.cell_size + 1,
                tile.row * self.cell_size + 1,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(window, self.colors[self.block_id], tile_rect)    