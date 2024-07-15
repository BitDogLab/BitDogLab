# 2048 Logic.py

import random

class Logic:
    
    # constants
    WON = 1
    GAME_NOT_OVER = 2
    LOST = 3
    
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    
    # current board matrix
    mat = []
    
    # list of board moves for animation
    moves = []
    
    def reset_game(self):
        # 4 columns by 4 rows board filled with blanks [1].
        self.mat = []
        for i in range(4):
            self.mat.append([1] * 4)

        # a new block to start the game with [2]
        self.add_new_block()
        
        # add frame to display
        self.moves.append(self.mat_copy(self.mat))
    # add new [2] block in a
    # random empty cell
    def add_new_block(self):

        j = random.randint(0, 3)
        i = random.randint(0, 3)

        while(self.mat[i][j] != 1):
            j = random.randint(0, 3)
            i = random.randint(0, 3)

        self.mat[i][j] = 2

    # function to get the current
    # state of game
    def get_current_state(self):

        # reached 2048 - win
        for j in range(4):
            for i in range(4):
                if(self.mat[i][j]== 2048):
                    return self.WON

        # blank cells - game isn't over
        for j in range(4):
            for i in range(4):
                if(self.mat[i][j] == 1):
                    return self.GAME_NOT_OVER

        # any adjustent cells with the same value - game isn't over
        for j in range(4):
            for i in range(3):
                if self.mat[i][j] == self.mat[i + 1][j]:
                    return self.GAME_NOT_OVER

        for j in range(3):
            for i in range(4):
                if self.mat[i][j]== self.mat[i][j + 1]:
                    return self.GAME_NOT_OVER
        
        # otherwise - game over
        return self.LOST

    def mat_copy(self, mat):
        temp = []
        for i in range(4):
            temp.append([1, 1, 1, 1])
            
        for j in range(4):
            for i in range(4):
                temp[i][j] = mat[i][j]
        
        return temp
    
    def rotate(self, mat):
        return [[mat[3-j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

    def move_align(self, changed):
        # align left
        animate = False
        for r in range(4):
            for j in range(4):
                for i in range(3):
                    if self.mat[i][j] == 1 and self.mat[i][j] != self.mat[i + 1][j]:
                        self.mat[i][j] = self.mat[i + 1][j]
                        self.mat[i + 1][j] = 1
                        changed = True
                        animate = True
            if animate:
                self.moves.append(self.mat_copy(self.mat))
                animate = False
        return changed
    
    def move_merge(self, changed):
        # merged blocks from right to left, don't merge a block that was already merged in this turn
        animate = False
        for j in range(4):
            merged = False
            for i in range(3):
                if not merged: #if block wasn't already merged
                    if self.mat[i][j] == self.mat[i+1][j] and self.mat[i][j] != 1:
                        self.mat[i][j] += self.mat[i+1][j]
                        self.mat[i+1][j] = 1
                        merged = True
                        changed = True
                else: # skip and allow merge the next block
                    merged = False
                    animate = True
        if animate:
            self.moves.append(self.mat_copy(self.mat))
        return changed

    def move(self, r):     
        self.moves = []
        if r > 0:
            for i in range(r):
                self.mat = self.rotate(self.mat_copy(self.mat))
        
        changed = self.move_align(False)
        changed = self.move_merge(changed)
        changed = self.move_align(changed)

        if changed:
            self.add_new_block()

        self.moves.append(self.mat_copy(self.mat))

        if r > 0:
            for i in range(4 - r):
                self.mat = self.rotate(self.mat_copy(self.mat))
            for el in range(len(self.moves)):
                for i in range(4 - r):
                    self.moves[el] = self.rotate(self.mat_copy(self.moves[el]))
        
        return changed
        
    # initialize game
    def __init__(self):
        self.reset_game()
        return