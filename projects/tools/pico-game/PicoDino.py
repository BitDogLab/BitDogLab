# PicoDino.py by Kobi Tyrkel
# A simple dino game
# for the Rapsberry Pi Pico RetroGaming Console

from PicoGame import PicoGame
from DinoGame.Resources import Resources
from DinoGame.Dino import Dino
from DinoGame.Cactus import Cactus
from DinoGame.Bird import Bird
from DinoGame.Dirt import Dirt
import time
import random

# init game
game = PicoGame()

def collide(s1, s2):
    # return true if two sprites has any pixels collide
    return game.sprites_collision(s1.get_sprite(), s1.x, s1.y, s2.get_sprite(), s2.x, s2.y)

def pico_dino_main():
    # Pico Dino main
    
    # Game settings
    SCREEN_WIDTH = game.SCREEN_WIDTH
    SCREEN_HEIGHT = game.SCREEN_HEIGHT

    PLAYER_SPEED = 3   # player speed along X in pixels per loop

    # initialize the game
    dino = Dino()
    cactus = Cactus()
    dirt1 = Dirt(32, 52, 1)
    dirt2 = Dirt(40, 57, 2)
    dirt3 = Dirt(48, 62, 3)
    bird = Bird()
    
    sound_freq = 180 # Sound frequency in Hz
    score = 0
    
    dino.sprites.append(game.add_sprite(Resources.DINO_A, Resources.DINO_A_W, Resources.DINO_A_H)) # Sprite 0
    dino.sprites.append(game.add_sprite(Resources.DINO_B, Resources.DINO_B_W, Resources.DINO_B_H)) # Sprite 1
    dino.sprites.append(game.add_sprite(Resources.DINO_C, Resources.DINO_C_W, Resources.DINO_C_H)) # Sprite 2
    dino.sprites.append(game.add_sprite(Resources.DINO_D, Resources.DINO_D_W, Resources.DINO_D_H)) # Sprite 3
    dino.sprites.append(game.add_sprite(Resources.DINO_E, Resources.DINO_E_W, Resources.DINO_E_H)) # Sprite 4
    dino.sprites.append(game.add_sprite(Resources.DINO_F, Resources.DINO_F_W, Resources.DINO_F_H)) # Sprite 5
    game.add_sprite(Resources.GROUND_LINE, Resources.GROUND_LINE_W, Resources.GROUND_LINE_H) # Sprite 6
    cactus.sprites.append(game.add_sprite(Resources.CACTUS_A, Resources.CACTUS_A_W, Resources.CACTUS_A_H)) # Sprite 7
    bird.sprites.append(game.add_sprite(Resources.BIRD_A, Resources.BIRD_A_W, Resources.BIRD_A_H)) # Sprite 8
    bird.sprites.append(game.add_sprite(Resources.BIRD_B, Resources.BIRD_B_W, Resources.BIRD_B_H)) # Sprite 9
    dirt1.sprites.append(game.add_sprite(Resources.DIRT_A, Resources.DIRT_A_W, Resources.DIRT_A_H)) # Sprite 10
    dirt2.sprites.append(game.add_sprite(Resources.DIRT_B, Resources.DIRT_B_W, Resources.DIRT_B_H)) # Sprite 11
    dirt3.sprites.append(game.add_sprite(Resources.DIRT_C, Resources.DIRT_C_W, Resources.DIRT_C_H)) # Sprite 12
    game.add_sprite(Resources.HEART, Resources.HEART_W, Resources.HEART_H) # Sprite 13
    
    dirt1.sprites.append(dirt2.get_sprite())
    dirt1.sprites.append(dirt3.get_sprite())
    dirt2.sprites.append(dirt3.get_sprite())
    dirt2.sprites.append(dirt1.get_sprite())
    dirt3.sprites.append(dirt1.get_sprite())
    dirt3.sprites.append(dirt2.get_sprite())
    
    
    # game loop
    while True:
        # move player
        dino.update()
        cactus.update()
        dirt1.update()
        dirt2.update()
        dirt3.update()
        
        if bird.x < cactus.x:
            bird.update()
            bird.update()
        if bird.x > cactus.x + 95:
            bird.update()
        
        if cactus.x < -31:
            score += 100
        
        if game.button_left():
            # left button pressed
            dino.move(PLAYER_SPEED)
                        
        elif game.button_right():
            # right button pressed
            dino.move(-PLAYER_SPEED)

        if game.button_down():
            dino.duck()

        if game.button_up() or game.button_A() or game.button_B():
            # button A or B pressed
            dino.jump()      
     
        game_over = False
        
        if collide(dino, cactus) or collide(dino, bird):
            dino.lives -= 1
            dino.state = Dino.DEAD
            if dino.lives <= 0:
                game_over = True
            else:
                dino.state = Dino.DEAD
                
        # refresh the display
        
        # clear the screen
        game.fill(0)
        
        # print the score
        game.top_right_corner_text(str(score))
        
        # draw hearts according to current dino lives
        if dino.lives > 0:
            game.sprite(13, 0, 0)
        if dino.lives > 1:
            game.sprite(13, 10, 0)
        if dino.lives > 2:
            game.sprite(13, 20, 0)
            
        # draw the player    
        game.sprite(dino.get_sprite(), dino.x, dino.y)
        
        # draw the ground and dirt
        game.sprite(6, 0, 48)
        game.sprite(dirt1.get_sprite(), dirt1.x, dirt1.y)
        game.sprite(dirt2.get_sprite(), dirt2.x, dirt2.y)
        game.sprite(dirt3.get_sprite(), dirt3.x, dirt3.y)
        
        # draw the cactus
        game.sprite(cactus.get_sprite(), cactus.x, cactus.y)
        
        #draw the bird
        game.sprite(bird.get_sprite(), bird.x, bird.y)
        
        # show the screen
        game.show()
        
        # no sound
        game.sound(0)
        
        if game_over:
            # play an ugly sound
            game.sound(200)
            time.sleep(0.5)
            game.sound(0)
            
            # display Game Over screen
            game.rect(0, 22, 128, 11, 1, True)
            
            game.center_text("GAME OVER", 0)
            game.top_right_corner_text(str(score))
            game.show()
            
            # wait for a button
            while not game.any_button():
                time.sleep(0.001)
            break
        else:
            if dino.state == Dino.DEAD:
                # play an ugly sound
                game.sound(200)
                time.sleep(0.5)
                game.sound(0)
                while not game.any_button():
                    time.sleep(0.001)
                dino.state = Dino.FALL
                bird.x = 512
                cactus.x = 256
            # quit
            
   
if __name__ == "__main__":
    pico_dino_main()

