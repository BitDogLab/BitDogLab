# PicoTetris.py by Kobi Tyrkel
# A simple tetris game
# for the Rapsberry Pi Pico RetroGaming Console

from PicoGame import PicoGame
from TetrisGame.Resources import Resources
from TetrisGame.Logic import Logic
import time
import random

# init game
game = PicoGame()
l = Logic()
sprites = []
sprites.append(game.add_sprite(Resources.BLOCK_0, Resources.BLOCK_0_W, Resources.BLOCK_0_H))
sprites.append(game.add_sprite(Resources.BLOCK_1, Resources.BLOCK_1_W, Resources.BLOCK_1_H))
sprites.append(game.add_sprite(Resources.BLOCK_2, Resources.BLOCK_2_W, Resources.BLOCK_2_H))
sprites.append(game.add_sprite(Resources.BLOCK_3, Resources.BLOCK_3_W, Resources.BLOCK_3_H))
key_down = True

def reset():
    l.reset()

def render():
    top_left = 1 #int(Resources.SCREEN_WIDTH / 2 - Resources.BLOCK_0_W * l.BOARD_WIDTH / 2)
    board_width = int(Resources.BLOCK_0_W * l.BOARD_WIDTH + 2)
    board_height = int(Resources.BLOCK_0_H * (l.BOARD_HEIGHT - 1))
    score = "Scr: "
    for i in range(0, 5 - len(str(l.score))):
        score = score + "0"
    score = score + str(l.score)
    level = "Lvl: "
    
    for i in range(0, 5 - len(str(l.level))):
        level = level + " "
    level = level + str(l.level)
    next_block = "Next:"
    game.fill(0)
    game.rect(top_left - 1, -1, 2 + Resources.BLOCK_0_W * l.BOARD_WIDTH, board_height + 2, 1)
    game.text(score, board_width + Resources.BLOCK_0_W, 0, 1)
    game.text(level, board_width + Resources.BLOCK_0_W, Resources.BLOCK_0_H * 2, 1)
    game.text(next_block, board_width + Resources.BLOCK_0_W, Resources.BLOCK_0_H * 4, 1)
    if game.__mute:
        game.text("Mute (B)", board_width + Resources.BLOCK_0_W, board_height - 5 * Resources.BLOCK_0_H, 1)
    for j in range(len(l.SHAPES[l.next_shape][0])):
        for i in range(len(l.SHAPES[l.next_shape][0][0])):
            if l.SHAPES[l.next_shape][0][j][i] != 0:
                game.rect(board_width + (len(l.SHAPES[l.next_shape][0][j]) + i) * Resources.BLOCK_0_W, int(board_height / 2 - Resources.BLOCK_0_H * j) , Resources.BLOCK_0_W, Resources.BLOCK_0_H, 1)
                
    for j in range(len(l.board)):
        for i in range(len(l.board[j])):
            if key_down == True:
                print(l.board[j][i], end=" ")
            if l.board[j][i] > 0:
            #   game.pixel(board_width + i, we might was to get some,  M0, 1)
                game.rect(top_left + i * game.sprite_width(l.board[j][i]), board_height -1 - (j + 4) * game.sprite_height(l.board[j][i]), 3, 3, 1)
        if key_down == True:
            print()
    if key_down == True:
        print(l.shape_x, l.shape_y, l.shape, l.shape_frame)
    if l.game_over:
        game.fill_rect(0, int(Resources.SCREEN_HEIGHT / 2) - Resources.BLOCK_0_W * 3, Resources.SCREEN_WIDTH, Resources.BLOCK_0_W * 4, 1)
        game.center_text("GAME OVER", 0)
    game.show()
    return

def handle_keys():
    global key_down
    while key_down == True:
        time.sleep(0.1)
        key_down = game.any_button()
    if game.button_down() == True:
        l.shape_y -= 1
        l.time_between_falls = 10
        key_down = True
    elif game.button_left() == True:
        l.shape_x -= 1
        key_down = True
    elif game.button_right() == True:
        l.shape_x += 1
        key_down = True
    elif game.button_up():
        l.set_level(l.level)
        key_down = True
    elif game.button_A(): # or game.button_up():
        l.shape_frame += 1
        key_down = True
    elif game.button_B():
        game.sound(0)
        game.__mute = not game.__mute
        key_down = True
    return

def play_tune_notes(notes, pace, beat):
    if beat >= len(notes):
        return -1
    game.sound(notes[beat][0])
    return int(pace / notes[beat][1])

def pico_tetris_main():
    reset()
    beat = 0
    next_beat = 0
    
    while True:
        current_time = time.ticks_ms()
        if current_time > next_beat:
            next_beat = current_time + play_tune_notes(Resources.TETRIS_THEME, 800, beat)
            beat += 1
            if next_beat < current_time:
                next_beat = 0
                beat = 0
        if not l.game_over:
            handle_keys()
            l.update()
            render()
        else:
            if game.any_button():
                game.sound(0)
                break
        
    
if __name__ == "__main__":
    pico_tetris_main()