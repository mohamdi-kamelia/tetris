# tetris.py
import pygame
from grid import Grid
from Blocks import *

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = Grid()
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        # Logique pour créer une nouvelle pièce (utilisez votre propre logique)
        pass

    def move_left(self):
        # Logique pour déplacer la pièce à gauche
        pass

    def move_right(self):
        # Logique pour déplacer la pièce à droite
        pass

    def move_down(self):
        # Logique pour déplacer la pièce vers le bas
        pass

    def rotate(self):
        # Logique pour faire tourner la pièce
        pass

    def update(self):
        # Logique pour mettre à jour le jeu (par exemple, détection de collision, suppression de lignes, etc.)
        pass

    def draw(self, window):
        # Logique pour dessiner la grille, la pièce en cours, etc.
        pass


"""
from grid import Grid
from Blocks import  *
from position import positions
import random
class  Game:
    def __init__(self):
        self.grid = Grid()
        self.Blocks = [IBlock(), JBlock() ,LBlock(), OBlock(), SBlock(), TBlock() , ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self):
        if len(self.Blocks) == 0:
            self.Blocks =  [IBlock(), JBlock() ,LBlock(), OBlock(), SBlock(), TBlock() , ZBlock()]
        block = random.choice(self.Blocks)
        self.Blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0 , -1)
        if self.block_inside() == False:
            self.current_block.move(0 , 1)
    
    def move_right(self):
        self.current_block.move(0 , 1)
        if self.block_inside() == False:
            self.current_block.move(0 , -1)
    
    def move_down(self):
        self.current_block.move(1 , 0)
        if self.block_inside() == False:
            self.current_block.move(-1 , 0)
    
    def block_inside(self):
        #position = positions(position.row + self.row_offset, position.column + self.column_offset)
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row , tile.column) == False:
                return False
        return True
    def draw(self, window):
        self.grid.draw(window)
        self.current_block.draw(window)
"""        