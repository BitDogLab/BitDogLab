# 2048 Logic.py

import random
import time

class Logic:

    # constants
    BOARD_HEIGHT = 20
    BOARD_WIDTH = 10
    
    WON = 1
    GAME_NOT_OVER = 2
    LOST = 3
    
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    
    COLORS = 4

    SHAPES = [            
        [
            [
                [0, 1],   #    []
                [0, 1],   #    []
                [1, 1]    #  [][]
            ],
            [
                [1, 0, 0],
                [1, 1, 1]
            ],
            [
                [1, 1],
                [1, 0],
                [1, 0]
            ],
            [
                [1, 1, 1],
                [0, 0, 1]
            ]
        ],
        [
            [
                [1, 0],   #  []
                [1, 0],   #  []
                [1, 1]    #  [][]
            ],
            [
                [1, 1, 1],
                [1, 0, 0]
            ],
            [
                [1, 1],
                [0, 1],
                [0, 1]
            ],
            [
                [0, 0, 1],
                [1, 1, 1]
            ]
        ],
        [
            [
                [1, 1, 0],   # [][]
                [0, 1, 1]    #   [][]
            ],
            [
                [0, 1],
                [1, 1],
                [1, 0]
            ]
        ],
        [            
            [
                [0, 1, 1],  #   [][]
                [1, 1, 0]   # [][]
            ],
            [
                [1, 0],
                [1, 1],
                [0, 1]
            ]
        ],
        [
            [
                [1, 1],   #  [][]
                [1, 1]    #  [][]
            ]
        ],
        [
            [
                [1, 1, 1, 1]
            ],
            [
                [1],    #  []
                [1],    #  []
                [1],    #  []
                [1]     #  []
            ]
        ],
        [
            [
                [0, 1, 0],  #    []
                [1, 1, 1]   #  [][][]
            ],
            [
                [1, 0],
                [1, 1],
                [1, 0]
            ],
            [
                [1, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 1],
                [1, 1],
                [0, 1]
            ]
        ]
    ]

    
    # game variables
    board = []
    next_shape = 0
    next_shape_color = 0
    shape = 0
    shape_color = 1
    shape_x = 0
    shape_y = 0
    shape_frame = 0
    
    shape_prev_x = 0
    shape_prev_y = 0
    shape_prev_frame = 0
    
    score = 0
    time_since_last_fall = 0
    time_between_falls = 700
    shape_changed = False
    level = 1
    game_over = False
    
    def set_level(self, level):
        self.level = level
        self.time_between_falls = max(770 - self.level * 70, 250)

    def pop_line(self, line):
        for j in range(line, len(self.board) - 1):
            for i in range(len(self.board[0])):
                self.board[j][i] = self.board[j + 1][i]
        self.board[len(self.board) - 1] = [0] * len(self.board[0])

    def scan_complete_rows(self):
        score = 0
        for j in range(len(self.board)):
            full_line = True
            for i in range(len(self.board[j])):
                if self.board[j][i] == 0:
                    full_line = False
            if full_line:
                self.pop_line(j)
                score += 100
                if score / 10 > self.level:
                    self.set_level(self.level + 1)
        return score
    
    def change_shape(self):
        self.shape = self.next_shape
        self.shape_color = self.next_shape_color
        self.next_shape = random.randint(0, len(self.SHAPES) - 1)
        self.shape_x = random.randint(0, self.BOARD_WIDTH - 4)
        self.next_shape_color = random.randint(1, self.COLORS - 1)
        self.shape_y = 16
        self.shape_frame = 0
        self.shape_prev_x = 0
        self.shape_prev_y = 16
        self.shape_prev_frame = 0
        self.shape_changed = True
        self.set_level(self.level)
        self.game_over = False
        for i in range(self.BOARD_WIDTH - 1):
            print(self.board[16])
            if self.board[16][i] != 0:
                self.game_over = True
        return

    def reset(self):
        # 4 columns by 4 rows board filled with blanks [1].
        self.board = []
        for i in range(self.BOARD_HEIGHT):
            self.board.append([0] * self.BOARD_WIDTH)
        # create the first two shapes
        self.change_shape()
        self.change_shape()
        return

    def update(self):
        if self.shape_changed:
            line_score = self.scan_complete_rows()
            self.score += line_score
            if line_score == 0:
                self.shape_changed = False
            return
        if time.ticks_ms() > self.time_since_last_fall + self.time_between_falls:
            self.time_since_last_fall = time.ticks_ms() + self.time_between_falls
            self.shape_y -= 1
            print("tick")
        new_shape = False
        # in case block hit ground, create a new shape
        if self.shape_y < 0:
            self.shape_y = 0
            new_shape = True
            print ("hit floor")
        # in case shape moved (x, y, frame) handle move
        if self.shape_x != self.shape_prev_x or self.shape_y != self.shape_prev_y or self.shape_frame != self.shape_prev_frame:
            # rotate frame as needed
            if self.shape_frame >= len(self.SHAPES[self.shape]):
                self.shape_frame = 0
            # don't allow move left beyond left wall
            if self.shape_x < 0:
                self.shape_x = 0
            # don't allow move right beyond right wall (consider shape width)
            if self.shape_x + len(self.SHAPES[self.shape][self.shape_frame][0]) > self.BOARD_WIDTH:
                print(len(self.SHAPES[self.shape][self.shape_frame][0]), self.SHAPES[self.shape][self.shape_frame][0])
                self.shape_x = self.shape_prev_x
                self.shape_frame = self.shape_prev_frame
            # remove previous shape from board 
            for j in range(0, len(self.SHAPES[self.shape][self.shape_prev_frame])):
                for i in range(0, len(self.SHAPES[self.shape][self.shape_prev_frame][j])):
                    if self.SHAPES[self.shape][self.shape_prev_frame][j][i] != 0:
                        self.board[self.shape_prev_y + j][self.shape_prev_x + i] = 0
            
            # check for collission with other blocks on board
            for j in range(0, len(self.SHAPES[self.shape][self.shape_frame])):
                for i in range(0, len(self.SHAPES[self.shape][self.shape_frame][j])):
                    if self.SHAPES[self.shape][self.shape_frame][j][i] != 0:
                        if self.board[self.shape_y + j][self.shape_x + i] != 0:
                            # undo move
                            self.shape_x = self.shape_prev_x
                            self.shape_frame = self.shape_prev_frame
                            print ("collission detected")
                            # if colission while going down, leave block in place
                            # and create a new one
                            if self.shape_y != self.shape_prev_y:
                                self.shape_y = self.shape_prev_y
                                new_shape = True
                                print ("landed on blocks")
            
            # no restrictions found,
            
            # draw shape in it's current position
            for j in range(0, len(self.SHAPES[self.shape][self.shape_frame])):
                for i in range(0, len(self.SHAPES[self.shape][self.shape_frame][j])):
                    if self.board[self.shape_y + j][self.shape_x + i] == 0:
                        self.board[self.shape_y + j][self.shape_x + i] = self.SHAPES[self.shape][self.shape_frame][j][i] * self.shape_color
            # set new position for comparison
            self.shape_prev_x = self.shape_x
            self.shape_prev_y = self.shape_y
            self.shape_prev_frame = self.shape_frame
            
        if new_shape:
            print ("new shape!")
            self.change_shape()
        
        return

    # initialize game
    def __init__(self):
        self.reset()
        return