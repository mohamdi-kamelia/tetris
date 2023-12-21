from grid import Grid
from Blocks import  *
import random
class  Game:
    def __init__(self, window_height, window_width):
        self.grid = Grid()
        self.Blocks = [IBlock(), JBlock() ,LBlock(), OBlock(), SBlock(), TBlock() , ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.window_width = window_width
        self.window_height = window_height
        #self.move_left_pressed = False
        #self.move_right_pressed = False
        #self.move_down_pressed = False

    def handle_input(self):
        if self.move_left:
            self.move_left()

        if self.move_right:
            self.move_right()

        if self.move_down:
            self.move_down()    

    def get_random_block(self):
        if len(self.Blocks) == 0:
            self.Blocks =  [IBlock(), JBlock() ,LBlock(), OBlock(), SBlock(), TBlock() , ZBlock()]
        block = random.choice(self.Blocks)
        self.Blocks.remove(block)
        return block
    
    def move_left(self):
        if self.block_inside(offset_columns=-1):
           if self.current_block.column_offset > 0:
               self.current_block.move(0, -1)

    def move_right(self):
        if self.block_inside(offset_columns=1):
            #if self.current_block.column_offset + self.current_block.get_max_column() < self.window_width / self.grid.cell_size - 1:
                self.current_block.move(0, 1)  

    def move_down(self):
        if self.block_inside(offset_rows=1):
            self.current_block.move(1, 0)
        else:
            # Si le bloc ne peut pas descendre, placez-le sur la grille et générez un nouveau bloc
            self.grid.place_block(self.current_block)
            self.current_block = self.next_block
            self.next_block = self.get_random_block()                 

    #def move_left(self):
        #self.current_block.move(0 , -1)
        #if self.block_inside() == False:
            #self.current_block.move(0 , 1)
           
    #def move_right(self):
        #self.current_block.move(0 , 1)
        #if self.block_inside() == False:
            #self.current_block.move(0 , -1)
        
    #def move_down(self):
        #self.current_block.move(1 , 0)
        #if self.block_inside() == False:
            #self.current_block.move(-1 , 0)

    def block_inside(self, offset_rows=0, offset_columns=0):
        position = positions(self.current_block.row_offset + offset_rows, self.current_block.column_offset + offset_columns)
        #position = positions(position.row + self.row_offset, position.column + self.column_offset)
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not (0 <= tile.row + position.row < self.grid.num_rows and 0 <= tile.column + position.column < self.grid.num_cols):
                return False
        # Vérifiez la collision avec d'autres blocs dans la grille
        for tile in tiles:
            if not self.grid.is_inside(tile.row + position.row, tile.column + position.column) or \
               self.grid.grid[tile.row + position.row][tile.column + position.column] != 0:
                return False
        return True
            #if not (0 <= tile.column + position.column < self.window_width / self.grid.cell_size):
                #return False
            #if not self.grid.is_inside(tile.row + position.row, tile.column + position.column):
                #return False
        #return True



        #for tile in tiles:
            #if not self.grid.is_inside(tile.row + position.row, tile.column + position.column):
                #return False
            #return True
    def draw(self, window):
        self.grid.draw(window)
        self.current_block.draw(window)





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