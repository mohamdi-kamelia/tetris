import pygame
from colors import colors

class Grid:
    def __init__(self):
    # Initialise la grille avec 20 lignes, 10 colonnes, et une taille de cellule de 30 pixels
        self.num_rows = 21
        self.num_cols = 13
        self.cell_size = 31
    # Initialise la grille à zéro (aucune cellule activée)
        self.grid = [[ 0 for j in range(self.num_cols)] for i in range (self.num_rows)]
    # Initialise une liste de couleurs pour les différentes cellules
        self.colors = colors.get_cell_colors()

    def print_grid(self):
    # Affiche la grille dans la console (à des fins de débogage)
    
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()


    def draw(self, window):
    # Dessine la grille en utilisant Pygame    
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Crée un rectangle (cellule) à l'emplacement correspondant dans la grille            
                cell_rect = pygame.Rect(column*self.cell_size +1, row*self.cell_size  + 1,self.cell_size - 1, self.cell_size  - 1)
                pygame.draw.rect(window , self.colors[cell_value] , cell_rect)
    def place_block(self, block):
        for tile in block.cells[block.rotation_state]:
            row, col = tile.row, tile.column
            self.grid[row][col] = block.block_id
"""
import pygame
from colors import colors

class Grid:
    def __init__(self):
    # Initialise la grille avec 20 lignes, 10 colonnes, et une taille de cellule de 30 pixels
        self.num_rows = 21
        self.num_cols = 13
        self.cell_size = 31
    # Initialise la grille à zéro (aucune cellule activée)
        self.grid = [[ 0 for j in range(self.num_cols)] for i in range (self.num_rows)]
    # Initialise une liste de couleurs pour les différentes cellules
        self.colors = colors.get_cell_colors()

    def print_grid(self):
    # Affiche la grille dans la console (à des fins de débogage)
    
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()
            
    def is_inside(self , row , column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def draw(self, window):
    # Dessine la grille en utilisant Pygame    
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # Crée un rectangle (cellule) à l'emplacement correspondant dans la grille            
                cell_rect = pygame.Rect(column * self.cell_size +1, row * self.cell_size  + 1,self.cell_size - 1, self.cell_size  - 1)
                pygame.draw.rect(window , self.colors[cell_value] , cell_rect)
    def place_block(self, block):
        for tile in block.cells[block.rotation_state]:
            row, col = tile.row, tile.column
            self.grid[row][col] = block.block_id
""" 
         