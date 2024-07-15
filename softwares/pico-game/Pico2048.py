# Pico2048.py migrated by Kobi Tyrkel
# A simple 2048 game migrated 
# for the Rapsberry Pi Pico RetroGaming Console

from PicoGame import PicoGame
from P2048.Logic import Logic
from P2048.Resources import Resources
import time

X_SHIFT = 32

# init game
game = PicoGame()
l = Logic()

sprites = []
sprites.append(game.add_sprite(Resources.A_0, Resources.A_0_W, Resources.A_0_H)) # sprite 0
sprites.append(game.add_sprite(Resources.A_2, Resources.A_2_W, Resources.A_2_H)) # sprite 1
sprites.append(game.add_sprite(Resources.A_4, Resources.A_4_W, Resources.A_4_H)) # sprite 2
sprites.append(game.add_sprite(Resources.A_8, Resources.A_8_W, Resources.A_8_H)) # sprite 3
sprites.append(game.add_sprite(Resources.A_16, Resources.A_16_W, Resources.A_16_H)) # sprite 4
sprites.append(game.add_sprite(Resources.A_32, Resources.A_32_W, Resources.A_32_H)) # sprite 5
sprites.append(game.add_sprite(Resources.A_64, Resources.A_64_W, Resources.A_64_H)) # sprite 6
sprites.append(game.add_sprite(Resources.A_128, Resources.A_128_W, Resources.A_128_H)) # sprite 7
sprites.append(game.add_sprite(Resources.A_256, Resources.A_256_W, Resources.A_256_H)) # sprite 8
sprites.append(game.add_sprite(Resources.A_512, Resources.A_512_W, Resources.A_512_H)) # sprite 9
sprites.append(game.add_sprite(Resources.A_1024, Resources.A_1024_W, Resources.A_1024_H)) # sprite 10
sprites.append(game.add_sprite(Resources.A_2048, Resources.A_2048_W, Resources.A_2048_H)) # sprite 11

def animate_moves(moves):
    for mat in moves:
        game.fill(0)
        for i in range(4):
            for j in range(4):
                for s_i in range(0, 12):
                    if mat[i][j] == 2 ** s_i:
                        game.sprite(sprites[s_i], X_SHIFT + i * game.sprite_width(sprites[s_i]), j * game.sprite_height(sprites[s_i]))
                        break;        
        game.show()
        time.sleep_ms(10)      

def play_tune(tune):
    for el in tune:
        game.sound(el[0])
        time.sleep_ms(int(800/el[1]) - 50)
        game.sound(0)
        time.sleep_ms(50)

def game_over():
    l.moves.append(l.mat_copy(l.mat))
    end_game_tune = True
    toggle_end_message = False
    while True:
        toggle_end_message = not toggle_end_message
        animate_moves(l.moves)
        if toggle_end_message:
            game.rect(0, 22, 128, 11, 1, True)
            if l.get_current_state() == Logic.WON:
                game.center_text("YOU WIN!", 0)
                if end_game_tune:
                    end_game_tune = False
                    play_tune(Resources.WIN_TUNE)
            else:
                game.center_text("YOU LOSE", 0)
                if end_game_tune:
                    end_game_tune = False
                    play_tune(Resources.GAME_OVER_TUNE)
        game.show()
        count_down = 10
        while count_down > 0:
            count_down -= 1
            time.sleep_ms(100)
            if game.any_button():
                break;
        if game.any_button():
            break;

def leave_game():
    l.moves.append(l.mat_copy(l.mat))
    toggle_message = False
    while True:
        toggle_message = not toggle_message
        animate_moves(l.moves)
        if toggle_message:
            game.rect(0, 22, 128, 11, 1, True)
            game.center_text("CLICK A TO LEAVE", 0)
        game.show()
        count_down = 10
        while count_down > 0:
            count_down -= 1
            time.sleep_ms(100)
            if game.any_button():
                if game.button_A():
                    return True
                return False
        
def pico_2048_main():
    # Pico 2048 main
    # Game settings
    
    if l.get_current_state() != Logic.GAME_NOT_OVER:
        l.reset_game()
    
    clicked = False
    
    # game loop
    while True:
        if game.button_down():
            clicked = True
            l.move(Logic.DOWN)
            
        if game.button_up():
            clicked = True
            l.move(Logic.UP)
            
        if game.button_right():
            clicked = True
            l.move(Logic.RIGHT)
        
        if game.button_left():
            clicked = True
            l.move(Logic.LEFT)
        
        if game.button_A():
            clicked = True
            if leave_game():
                break
        
        if (len(l.moves) > 0):
            animate_moves(l.moves)
            l.moves = []
        
        # wait for a clicked key to be released
        while (clicked):
            time.sleep_ms(100)
            if not game.any_button():
                clicked = False
        
        if l.get_current_state() != Logic.GAME_NOT_OVER:
            game_over()
            break
            
if __name__ == "__main__":
    pico_2048_main()