class Resources:
    
    # Constants
    SCREEN_WIDTH = 128
    SCREEN_HEIGHT = 64
    
    NOTE = {" " : 0,
            "a" : 440,
            "b" : 493,
            "c" : 523,
            "d" : 587,
            "e" : 659,
            "f" : 698,
            "g" : 207,
            "A" : 880,
            "B" : 246,
            "C" : 261,
            "D" : 293,
            "E" : 329,
            "F" : 349,
            "G" : 415,
            "X" : 220
            }
    
    # Tunes
    WIN_TUNE = [
        (NOTE["e"], 16),
        (NOTE[" "], 16),
        (NOTE[" "], 16),
        (NOTE["c"], 16),
        (NOTE["d"], 16),
        (NOTE[" "], 16)
        ]
    
    GAME_OVER_TUNE = [
        (NOTE["C"], 4),
        (NOTE["X"], 4),
        (NOTE["F"], 4),
        (NOTE[" "], 4),
        (NOTE["X"], 2)
        ]
    
    TETRIS_THEME = [
        (NOTE["e"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["c"], 4),
        (NOTE["b"], 4),
        (NOTE["a"], 2),
        (NOTE["a"], 4),
        (NOTE["c"], 4),
        (NOTE["e"], 2),
        (NOTE["d"], 4),
        (NOTE["c"], 4),
        (NOTE["b"], 2),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["e"], 2),
        (NOTE["c"], 2),
        (NOTE["a"], 2),
        (NOTE["a"], 4),
        (NOTE["a"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        
        (NOTE["d"], 4),
        (NOTE["f"], 4),
        (NOTE["A"], 2),
        (NOTE["G"], 4),
        (NOTE["f"], 4),
        (NOTE["e"], 2),
        (NOTE["c"], 4),
        (NOTE["e"], 2),
        (NOTE["d"], 4),
        (NOTE["c"], 4),
        (NOTE["b"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["e"], 2),
        (NOTE["c"], 2),
        (NOTE["a"], 2),
        (NOTE["a"], 2),
        (NOTE[" "], 2),

        (NOTE["e"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["c"], 4),
        (NOTE["b"], 4),
        (NOTE["a"], 2),
        (NOTE["a"], 4),
        (NOTE["c"], 4),
        (NOTE["e"], 2),
        (NOTE["d"], 4),
        (NOTE["c"], 4),
        (NOTE["b"], 2),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["e"], 2),
        (NOTE["c"], 2),
        (NOTE["a"], 2),
        (NOTE["a"], 4),
        (NOTE["a"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        
        (NOTE["d"], 4),
        (NOTE["f"], 4),
        (NOTE["A"], 2),
        (NOTE["G"], 4),
        (NOTE["f"], 4),
        (NOTE["e"], 2),
        (NOTE["c"], 4),
        (NOTE["e"], 2),
        (NOTE["d"], 4),
        (NOTE["c"], 4),
        (NOTE["b"], 2),
        (NOTE["b"], 4),
        (NOTE["c"], 4),
        (NOTE["d"], 2),
        (NOTE["e"], 2),
        (NOTE["c"], 2),
        (NOTE["a"], 2),
        (NOTE["a"], 2),
        (NOTE[" "], 2),
        
        (NOTE["E"], 1),
        (NOTE["C"], 1),
        (NOTE["D"], 1),
        (NOTE["B"], 1),
        (NOTE["C"], 1),
        (NOTE["X"], 1),
        (NOTE["g"], 1),
        (NOTE["B"], 2),
        (NOTE[" "], 4),
        (NOTE["E"], 1),
        (NOTE["C"], 1),
        (NOTE["D"], 1),
        (NOTE["B"], 1),
        (NOTE["C"], 2),
        (NOTE["E"], 2),
        (NOTE["a"], 1),
        (NOTE["G"], 1),
        (NOTE[" "], 4)
        ]
    
    # Sprites graphics definition
    BLOCK_0_W = 4    # width and height of the sprite in pixels
    BLOCK_0_H = 4
    BLOCK_0 = bytearray([
        0b0000,
        0b0000,
        0b0000,
        0b0000
        ])
    BLOCK_1_W = 4    # width and height of the sprite in pixels
    BLOCK_1_H = 4
    BLOCK_1 = bytearray([
        0b0110,
        0b1001,
        0b1001,
        0b0110
        ])
    BLOCK_2_W = 4    # width and height of the sprite in pixels
    BLOCK_2_H = 4
    BLOCK_2 = bytearray([
        0b0110,
        0b1101,
        0b1011,
        0b0110
        ])
    BLOCK_3_W = 4    # width and height of the sprite in pixels
    BLOCK_3_H = 4
    BLOCK_3 = bytearray([
        0b0110,
        0b1011,
        0b1101,
        0b0110
        ])