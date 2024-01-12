from grid import Grid
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from blocks import *
=======
from Blocks import *
>>>>>>> kamelia
=======
from Blocks import *
>>>>>>> b2630b668300a89442fed2605a4767503812117b
=======
from Blocks import *
>>>>>>> kamelia
import random 
import pygame
class Game : 
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg.mp3")
        self.game_over_sound = pygame.mixer.Sound("Sounds/Game Over.mp3")
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1)
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared ==  3:
            self.update_score += 500
        self.score += move_down_points
    def get_random_block(self):
        if len(self.blocks) == 0 :
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    def move_left(self):
        self.current_block.move(0 , -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)
    def move_right(self):
        self.current_block.move(0 , 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)
    def move_down(self):
        self.current_block.move(1 , 0)
        if self.block_inside() == False or self.block_fits() == False : 
            self.current_block.move(-1, 0)
            self.lock_block()
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)
        if self.block_fits() == False:
            self.game_over = True
            self.game_over_sound.play()
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles :
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()

    def draw(self, window):
        self.grid.draw(window)
        self.current_block.draw(window, 11, 11)
        if self.next_block.id == 3:
            self.next_block.draw(window, 355 , 250 )
        elif self.next_block.id == 4:
            self.next_block.draw(window , 390, 280 )
        else:
<<<<<<< HEAD
<<<<<<< HEAD
            self.next_block.draw(window, 370, 270 )
=======
            self.next_block.draw(window, 370, 270 ) 

>>>>>>> kamelia
=======
            self.next_block.draw(window, 370, 270 ) 

>>>>>>> kamelia

