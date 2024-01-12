from colors import Colors
from position import Position
import pygame

class Block:
<<<<<<< HEAD
    def __init__(self, id):
        """
        Initialise un objet Block avec un identifiant unique (block_id).

        Parameters:
        - block_id (int): Identifiant du bloc.
        """ 
=======
    def __init__(self, id): 
>>>>>>> kamelia
        self.id = id
        self.cells = {} 
        self.cell_size = 31
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0  
        self.colors = Colors.get_cell_colors()
        
    def move(self , rows , columns):
<<<<<<< HEAD
        """
        Déplace le bloc de la quantité spécifiée de lignes et de colonnes.

        Parameters:
        - rows (int): Nombre de lignes à déplacer.
        - columns (int): Nombre de colonnes à déplacer.
        """
        self.row_offset += rows
        self.column_offset += columns
    def get_cell_positions(self):
        """
        Retourne les positions des cellules du bloc en prenant en compte le décalage et la rotation.

        Returns:
        List[Position]: Liste des positions des cellules.
        """
        tiles = self.cells[self.rotation_state] 
=======
         self.row_offset += rows
         self.column_offset += columns
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
>>>>>>> kamelia
        moved_tiles = []
        for position in tiles :
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    def rotate(self):
<<<<<<< HEAD
        """
        Effectue une rotation du bloc dans le sens horaire.
        """
=======
>>>>>>> kamelia
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    def undo_rotation(self):
<<<<<<< HEAD
        """
        Annule la dernière rotation effectuée sur le bloc.
        """
=======
>>>>>>> kamelia
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, window, offset_x , offset_y):
<<<<<<< HEAD
        """
        Dessine le bloc sur la fenêtre spécifiée avec les décalages spécifiés.

        Parameters:
        - window (pygame.Surface): Surface de la fenêtre pour dessiner.
        - offset_x (int): Décalage horizontal.
        - offset_y (int): Décalage vertical.
        """
        tiles = self.get_cell_positions()  # Utilisez get pour éviter une clé manquante
        for tile in tiles:
                tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size , offset_y + tile.row * self.cell_size , self.cell_size - 1, self.cell_size - 1)
<<<<<<< HEAD
                pygame.draw.rect(window, self.colors[self.id], tile_rect) 
=======
=======
        tiles = self.get_cell_positions()  # Utilisez get pour éviter une clé manquante
        for tile in tiles:
                tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size , offset_y + tile.row * self.cell_size , self.cell_size - 1, self.cell_size - 1)
>>>>>>> kamelia
                pygame.draw.rect(window, self.colors[self.id], tile_rect) 


 

<<<<<<< HEAD
>>>>>>> kamelia
=======
>>>>>>> kamelia
