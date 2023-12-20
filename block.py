import pygame
from colors import Colors
from position import positions

class Block:
    def __init__(self, block_id):  
        self.cell_size = 31
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

        # Assurez-vous que self.block_id est un index valide pour self.colors
        if block_id < 0 or block_id >= len(self.colors):
            self.block_id = 0  # Vous pouvez choisir une valeur par défaut appropriée
        else:
            self.block_id = block_id

        # Supposons que self.cells est initialisé correctement ailleurs dans votre code
        self.cells = {}  
    
    def  move(self, rows, columns):  
        self.row_offset += rows
        self.column_offset += columns 

        for rotation_state, positions_list in self.cells.items():
            for position in positions_list:
                position.row += self.row_offset
                position.column += self.column_offset

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = position (position.row + self.row_offset, position.column +self.column_offset) 
            moved_tiles.append(positions) 
        return moved_tiles

    def draw(self, window):
        tiles = self.cells.get(self.rotation_state, [])  
        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(window, self.colors[self.block_id], tile_rect)


