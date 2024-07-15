# PicoInvaders.py by Vincent Mistler (YouMakeTech)
# A simplified Space Invaders game
# for the Rapsberry Pi Pico RetroGaming Console
#
# The code is far from perfect but it works!

from PicoGame import PicoGame
import time
import random

def intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    # return true if the 2 rectangles
    # (x1,y1,w1,h1) and (x2,y2,w2,h2) overlaps
    # this is used to detect collisions between sprites
    overlap = True
    if x2 > x1 + w1 - 1:
        overlap = False
    if x2 + w2 - 1 < x1:
        overlap = False
    if y2 > y1 + h1 -1:
        overlap = False
    if y2 + h2 -1 < y1:
        overlap = False
    return overlap

class Alien:
    # Alien states (constants)
    DEAD = 0       
    DISAPPEARING = 1
    EXPLODING = 2
    ALIVE = 3
    
    def __init__(self, x, y, sprite):
        self.x = x     # position of the alien on the screen
        self.y = y
        self.sprite = sprite # sprite number
        self.state = Alien.ALIVE
    
    def switch_sprite(self):
        # switch between sprites to animate aliens
        if self.sprite<3:
            self.sprite+=3
        else:
            self.sprite-=3

class Laser:
    def __init__(self, width, height):
        # initialize laser starting coordinates
        # from ship coordinates
        self.width = width
        self.height = height
        self.x = -1         # laser position on screen
        self.y = -1
        self.x0 = -1        # ship position when firing
        self.y0 = -1
        self.active = False # True whe a laser is displayed
        self.released = False   # True once right after firing
        
    def fire(self, x0, y0):
        if not self.active:
            self.x0 = x0
            self.y0 = y0
            self.x = x0 + 5
            self.y = y0
            self.active = True
        
    def move(self, vy):
        if self.active:
            self.y += vy
            if self.y < 0:
                self.active = False
            
    def draw(self, game):
        if self.active:
            game.fill_rect(int(self.x), int(self.y), self.width, self.height, 1)
    
class Ufo:
    # UFO states (constants)
    DEAD = 0       
    DISAPPEARING = 1
    EXPLODING = 2
    ALIVE = 3
    
    def __init__(self):
        self.x = -1     # position of the ufo on the screen
        self.y = -1
        self.state = Ufo.DEAD
        
    def move(self, vx):
        # move the UFO towards the right of the screen
        # at speed vx
        self.x += vx
        if self.x > 128:
            self.state = Ufo.DEAD

def init_aliens(ALIENS_ROWS,ALIENS_COLS,ALIENS_INIT_X,ALIENS_INIT_Y,ALIENS_SPACING_X,ALIENS_SPACING_Y):
    # initialize aliens
    aliens = []
    sprite = 0
    for i in range(ALIENS_ROWS):
        for j in range(ALIENS_COLS):
            x = ALIENS_INIT_X + j * ALIENS_SPACING_X
            y = ALIENS_INIT_Y + i * ALIENS_SPACING_Y
            alien = Alien(x, y, min(i,2))
            aliens.append(alien)
    return aliens

def pico_invaders_main():
    # Pico Invaders main
    
    game = PicoGame()
    
    # Sprites graphics definition
    ALIEN1A_W = 8    # width and height of the sprite in pixels
    ALIEN1A_H = 8
    ALIEN1A = bytearray([0b00011000,
                         0b00111100,
                         0b01111110,
                         0b11011011,
                         0b11111111,
                         0b00100100,
                         0b01011010,
                         0b10100101])

    ALIEN1B_W = 8
    ALIEN1B_H = 8
    ALIEN1B = bytearray([0b00011000,
                         0b00111100,
                         0b01111110,
                         0b11011011,
                         0b11111111,
                         0b01011010,
                         0b10000001,
                         0b01000010])


    ALIEN2A_W = 11
    ALIEN2A_H = 8
    ALIEN2A = bytearray([0b00100000,0b10000000,
                         0b00010001,0b00000000,
                         0b00111111,0b10000000,
                         0b01101110,0b11000000,
                         0b11111111,0b11100000,
                         0b10111111,0b10100000,
                         0b10100000,0b10100000,
                         0b00011011,0b00000000])

    ALIEN2B_W = 11
    ALIEN2B_H = 8
    ALIEN2B = bytearray([0b00100000,0b10000000,
                         0b10010001,0b00100000,
                         0b10111111,0b10100000,
                         0b11101110,0b11100000,
                         0b11111111,0b11100000,
                         0b00111111,0b10000000,
                         0b00100000,0b10000000,
                         0b01000000,0b01000000])

    ALIEN3A_W = 12
    ALIEN3A_H = 8
    ALIEN3A = bytearray([0b00001111,0b00000000,
                         0b01111111,0b11100000,
                         0b11111111,0b11110000,
                         0b11100110,0b01110000,
                         0b11111111,0b11110000,
                         0b00011001,0b10000000,
                         0b00110110,0b11000000,
                         0b11000000,0b00110000])

    ALIEN3B_W = 12
    ALIEN3B_H = 8
    ALIEN3B = bytearray([0b00001111,0b00000000,
                         0b01111111,0b11100000,
                         0b11111111,0b11110000,
                         0b11100110,0b01110000,
                         0b11111111,0b11110000,
                         0b00011001,0b10000000,
                         0b00110110,0b11000000,
                         0b00011001,0b10000000])

    PLAYER_W = 11
    PLAYER_H = 8
    PLAYER = bytearray([0b00000100,0b00000000,
                        0b00001110,0b00000000,
                        0b00001110,0b00000000,
                        0b01111111,0b11000000,
                        0b11111111,0b11100000,
                        0b11111111,0b11100000,
                        0b11111111,0b11100000,
                        0b11111111,0b11100000])

    LASER_W = 1
    LASER_H = 8
    LASER = bytearray([0b00000100,
                       0b00000100,
                       0b00000100,
                       0b00000100,
                       0b00000100,
                       0b00000100,
                       0b00000100,
                       0b00000100])

    EXPLOSION_W = 12
    EXPLOSION_H = 7
    EXPLOSION = bytearray([0b00001000,0b10000000,
                           0b01000101,0b00010000,
                           0b00100000,0b00100000,
                           0b00010000,0b01000000,
                           0b11000000,0b00011000,
                           0b00010000,0b01000000,
                           0b00100101,0b00100000,
                           0b01001000,0b10010000])

    UFO_W = 16
    UFO_H = 7
    UFO = bytearray([0b00000111,0b11100000,
                     0b00011111,0b11111000,
                     0b00111111,0b11111100,
                     0b01101101,0b10110110,
                     0b11111111,0b11111111,
                     0b00111001,0b10111000,
                     0b00010000,0b00010000,
                     0b00000000,0b00000000])
    
    # Game settings
    SCREEN_WIDTH = game.SCREEN_WIDTH
    SCREEN_HEIGHT = game.SCREEN_HEIGHT

    ALIENS_ROWS = 3    # How many rows and columns of aliens?
    ALIENS_COLS = 5
    ALIENS_SPACING_X = 20
    ALIENS_SPACING_Y = 10
    ALIENS_INIT_X = int(SCREEN_WIDTH/2 - ((ALIENS_COLS+1) * ALIENS_SPACING_X)/2)
    ALIENS_INIT_Y = 8
    ALIENS_VX = 1.0    # aliens speed along X and Y in pixels per loop
    ALIENS_VY = 2.0

    PLAYER_Y = SCREEN_HEIGHT - PLAYER_H # Vertical position of the player in pixels
    PLAYER_SPEED = 3.0   # player speed along X in pixels per loop

    LASER_WIDTH = 1      # laser width and height in pixels
    LASER_HEIGHT = 4
    LASER_SPEED = 4.0    # laser speed in pixels per loop

    UFO_X = 0            # UFO starting position on the screen in pixels
    UFO_Y = 0
    UFO_SPEED = 2.0      # UFO speed in pixels per loop
    
    # initialize the game
    aliens = init_aliens(ALIENS_ROWS,ALIENS_COLS,ALIENS_INIT_X,ALIENS_INIT_Y,ALIENS_SPACING_X,ALIENS_SPACING_Y)
    laser = Laser(LASER_WIDTH, LASER_HEIGHT)
    ufo = Ufo()
    aliens_vx = ALIENS_VX
    player_x = SCREEN_WIDTH/2 - PLAYER_W/2
    loop_counter = 0
    sound_freq = 180 # Sound frequency in Hz
    score = 0
    
    game.add_sprite(ALIEN1A, ALIEN1A_W, ALIEN1A_H) # Sprite 0
    game.add_sprite(ALIEN2A, ALIEN2A_W, ALIEN2A_H) # Sprite 1
    game.add_sprite(ALIEN3A, ALIEN3A_W, ALIEN3A_H) # Sprite 2
    game.add_sprite(ALIEN1B, ALIEN1B_W, ALIEN1B_H) # Sprite 3
    game.add_sprite(ALIEN2B, ALIEN2B_W, ALIEN2B_H) # Sprite 4
    game.add_sprite(ALIEN3B, ALIEN3B_W, ALIEN3B_H) # Sprite 5
    game.add_sprite(PLAYER, PLAYER_W, PLAYER_H)    # Sprite 6
    game.add_sprite(LASER, LASER_W, LASER_H)       # Sprite 7
    game.add_sprite(EXPLOSION, EXPLOSION_W, LASER_H)   # Sprite 8
    game.add_sprite(UFO, UFO_W, UFO_H)             # Sprite 9

    # game loop
    while True:
        # move player
        if game.button_left():
            # left button pressed
            # => move player ship to the left
            player_x -= PLAYER_SPEED
            # do not allow player to leave the screen!
            if player_x < 0:
                player_x = 0
        elif game.button_right():
            # right button pressed
            # => move player ship to the right
            player_x += PLAYER_SPEED
            # do not allow player to leave the screen!
            if player_x + PLAYER_W > SCREEN_WIDTH:
                player_x = SCREEN_WIDTH - PLAYER_W

        if game.button_A() or game.button_B():
            # button A or B pressed
            # fire a laser
            laser_active_prev=laser.active
            laser.fire(player_x, PLAYER_Y)
            if not laser_active_prev and laser.active:
                # make a sound when the laser is released
                game.sound(1000)
            
        # move the laser towards the top of the screen
        laser.move(-LASER_SPEED)
        
        
        if ufo.state != Ufo.ALIVE:
            # send an UFO ? (one chance in 500)
            if random.randint(0,500)==50:
                ufo.x = UFO_X
                ufo.y = UFO_Y
                ufo.state = Ufo.ALIVE
        else:
            # move the UFO
            ufo.move(UFO_SPEED)

            # play the UFO sound (alternate between 2 frequencies)
            if sound_freq == 1100:
                sound_freq = 2000
            else:
                sound_freq = 1100
            game.sound(sound_freq)
        
        # move aliens left/right and bottom when they hit
        # the left or right edge of the screen
        collision = False # collision with the edge of the screen?
        for alien in aliens:
            if alien.state == Alien.ALIVE:
                width = game.sprite_width(alien.sprite)
                height = game.sprite_height(alien.sprite)
                if aliens_vx > 0 and alien.x + aliens_vx + width > SCREEN_WIDTH:
                    # this allien hits the right edge of teh screen
                    collision = True
                    break
                elif aliens_vx<0 and alien.x + aliens_vx < 0:
                    # this allien hits the left edge of the screen
                    collision = True            
                    break
        if collision:
            # one alien hit the left or right edge of the screen
            # reverse x direction for all
            collision = True
            aliens_vx = - aliens_vx
            aliens_vy = ALIENS_VY
        else:
            aliens_vy = 0.0
        
        game_over = False
        for alien in aliens: 
            alien.x += aliens_vx
            alien.y += aliens_vy
            if alien.state == Alien.ALIVE and alien.y>SCREEN_HEIGHT:
                # Aliens reached the bottom of the screen
                # => Game Over
                game_over = True
        
        # detect collisions between laser and aliens
        # + player and aliens
        for alien in aliens:
            if alien.state == Alien.ALIVE:
                width = game.sprite_width(alien.sprite)
                height = game.sprite_height(alien.sprite)
                              
                if not game_over:
                    # check collision between player and alien
                    if intersect(player_x, PLAYER_Y, PLAYER_W, PLAYER_H, alien.x, alien.y, width, height):
                        # the player was hit by an alien
                        game_over = True
                
                if laser.active and intersect(laser.x, laser.y, laser.width, laser.height, alien.x, alien.y, width, height):
                    # laser hit an alien
                    alien.state = Alien.EXPLODING
                    laser.active = False # disable laser
                    score += 10
                    
        # detect collision between laser and ufo
        if laser.active and ufo.state == Ufo.ALIVE:
            if intersect(laser.x, laser.y, laser.width, laser.height, ufo.x, ufo.y, UFO_W, UFO_H):
                # laser hit the UFO
                ufo.state = Ufo.EXPLODING
                score += 100
        
        # actions that happen every 16 frames
        loop_counter += 1
        if (loop_counter%16) == 0:
            loop_counter = 0 # reset loop_counter
            
            # alternate between 2 sprites to animate aliens
            for alien in aliens:
                alien.switch_sprite()
                
            if ufo.state == Ufo.DEAD:
                # play Alien sounds
                if sound_freq == 180:
                    sound_freq = 160
                elif sound_freq == 160:
                    sound_freq = 140
                elif sound_freq == 140:
                    sound_freq = 120
                else:
                    sound_freq = 180
                game.sound(sound_freq)

        # refresh the display
        
        # clear the screen
        game.fill(0)
        
        # print the score
        game.top_right_corner_text(str(score))
        
        # draw the aliens
        for alien in aliens:
            if alien.state == Alien.ALIVE:
                # draw sprite
                game.sprite(alien.sprite, int(alien.x), int(alien.y))
            elif alien.state == Alien.EXPLODING:
                # Alien is exploding => draw explosion (sprite 8)
                game.sprite(8, int(alien.x), int(alien.y))
                alien.state = Alien.DISAPPEARING
                # and make explosion sound
                game.sound(800)
            elif alien.state == Alien.DISAPPEARING:
                # draw explosion slightly shifted (sprite 8)
                game.sprite(8, int(alien.x) + 2, int(alien.y) + 2)
                alien.state = Alien.DEAD
        
        # draw the player
        game.sprite(6, int(player_x), int(PLAYER_Y))
        
        # draw the laser
        laser.draw(game)
        
        # draw the UFO and update its state
        if ufo.state != Ufo.DEAD:
            if ufo.state == Ufo.ALIVE:
                game.sprite(9, int(ufo.x), int(ufo.y))
            elif ufo.state == Ufo.EXPLODING:
                # UFO is exploding => draw explosion (sprite 8)
                game.sprite(8, int(ufo.x), int(ufo.y))
                # and make explosion sound
                game.sound(500)
                ufo.state = Ufo.DISAPPEARING
            elif ufo.state == Ufo.DISAPPEARING:
                 # draw explosion slightly shifted (sprite 8)
                game.sprite(8, int(ufo.x) + 2, int(ufo.y) + 2)
                ufo.state = Ufo.DEAD

        # print the score
        game.top_right_corner_text(str(score))
        
        # show the screen
        game.show()
        
        # no sound
        game.sound(0)
        
        # Reset aliens when they are all dead
        at_least_one_alien_alive = False
        for alien in aliens:
            if alien.state == Alien.ALIVE:
                at_least_one_alien_alive = True
                break
        
        if not at_least_one_alien_alive:
            # No aliens remaining => send a new wave 
            aliens = init_aliens(ALIENS_ROWS,ALIENS_COLS,ALIENS_INIT_X,ALIENS_INIT_Y,ALIENS_SPACING_X,ALIENS_SPACING_Y)
            aliens_vx = aliens_vx * 1.2 # increases aliens velocity by +20%
        
        if game_over:
            # play an ugly sound
            game.sound(200)
            time.sleep(0.5)
            game.sound(0)
            
            # display Game Over screen
            game.fill(0)
            game.center_text("GAME OVER")
            game.top_right_corner_text(str(score))
            game.show()
            
            # wait for a button
            while not game.any_button():
                time.sleep(0.001)
            
            # quit
            break
            
   
if __name__ == "__main__":
    pico_invaders_main()
