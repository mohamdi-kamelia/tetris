
from block import Block
from position import positions

class LBlock(Block):
    def __init__(self):
        super().__init__(block_id = 1)  
        self.cells = {
            0: [positions(0, 2), positions(1, 0), positions(1, 1), positions(1, 2)],
            1: [positions(0, 1), positions(1, 1), positions(2, 1), positions(2, 2)],
            2: [positions(1, 0), positions(1, 1), positions(1, 2), positions(2, 0)],
            3: [positions(0, 0), positions(0, 1), positions(1, 1), positions(2, 1)]
        }
class JBlock(Block):
    def __init__(self):
        super().__init__(block_id = 2 ) 
        self.cells = {
            0: [positions(0, 0), positions(1, 0), positions(1, 1), positions(1, 2)],
            1: [positions(0, 1), positions(0, 2), positions(1, 1), positions(2, 1)],
            2: [positions(1, 0), positions(1, 1), positions(1, 2), positions(2, 2)],
            3: [positions(0, 1), positions(1, 1), positions(2, 0), positions(2, 1)]
        }
class IBlock(Block):
    def __init__(self):
        super().__init__(block_id = 3)  
        self.cells = {
            0: [positions(1, 0), positions(1, 1), positions(1, 2), positions(1, 3)],
            1: [positions(0, 2), positions(1, 2), positions(2, 2), positions(3, 2)],
            2: [positions(2, 0), positions(2, 1), positions(2, 2), positions(2, 3)],
            3: [positions(0, 1), positions(1, 1), positions(2, 1), positions(3, 1)]
        }
class OBlock(Block):
    def __init__(self):
        super().__init__(block_id = 4)  
        self.cells = {
            0: [positions(0, 0), positions(0, 1), positions(1, 0), positions(1, 1)],
        }
class SBlock(Block):
    def __init__(self):
        super().__init__(block_id = 5) 
        self.cells = {
            0: [positions(0, 1), positions(0, 2), positions(1, 0), positions(1, 1)],
            1: [positions(0, 1), positions(1, 1), positions(1, 2), positions(2, 2)],
            2: [positions(1, 1), positions(1, 2), positions(2, 0), positions(2, 1)],
            3: [positions(0, 0), positions(1, 0), positions(1, 1), positions(2, 1)]
        }
class TBlock(Block):
    def __init__(self):
        super().__init__(block_id = 7)  
        self.cells = {
            0: [positions(0, 1), positions(1, 0), positions(1, 1), positions(1, 2)],
            1: [positions(0, 1), positions(1, 1), positions(1, 2), positions(2, 1)],
            2: [positions(1, 0), positions(1, 1), positions(1, 2), positions(2, 1)],
            3: [positions(0, 1), positions(1, 0), positions(1, 1), positions(2, 1)]
        }
class ZBlock(Block):
    def __init__(self):
        super().__init__(block_id= 8)  
        self.cells = {
            0: [positions(0, 0), positions(0, 1), positions(1, 1), positions(1, 2)],
            1: [positions(0, 2), positions(1, 1), positions(1, 2), positions(2, 1)],
            2: [positions(1, 0), positions(1, 1), positions(2, 1), positions(2, 2)],
            3: [positions(0, 1), positions(1, 0), positions(1, 1), positions(2, 0)]
        }
