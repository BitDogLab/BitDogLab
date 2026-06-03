class Dino:
    # Dino states (constants)
    DEAD = 0       
    DUCK = 1
    JUMP = 2
    FALL = 3
    RUN = 4
    
    START_X = 20
    START_Y = 32
    
    def __init__(self):
        self.x = Dino.START_X     # position of the dino on the screen
        self.y = Dino.START_Y
        self.state = Dino.RUN
        self.sprite_index = 0
        self.ticker = 0
        self.duck_timer = 0
        self.lives = 3
        self.sprites = []
    
    def update(self):
        # count ticks for delayed animation
        self.ticker += 1
        if self.ticker > 15:
            self.ticker = 0
        if self.state == Dino.JUMP:
            self.y -= 1
        if self.y < 5:
            self.state = Dino.FALL
        if self.state == Dino.FALL:
            self.y += 1
        if self.state == Dino.FALL and self.y >= Dino.START_Y:
            self.state = Dino.RUN
            self.y = Dino.START_Y
        if self.state == Dino.DUCK:
            self.duck_timer -= 1
        if self.state == Dino.DUCK and self.duck_timer <= 0:
            self.state = Dino.RUN
        self.switch_sprite()

    def move(self, vx):
        # move the DINO
        # at speed vx
        self.x -= vx
        if self.x < 0:
            self.x = 0
        if self.x > 48:
            self.x = 48
            
    def jump(self):
        if self.state == Dino.RUN or self.state == Dino.DUCK:
            self.state = Dino.JUMP
    
    def duck(self):
        if self.state == Dino.RUN:
            self.state = Dino.DUCK
            self.duck_timer = 128
      
    def switch_sprite(self):
        # switch between sprites to animate cactus
        if self.state != Dino.DUCK:
            self.sprite_index = 0
            if self.ticker > 3:
                self.sprite_index = 1
            if self.ticker > 7:
                self.sprite_index = 0
            if self.ticker > 11:
                self.sprite_index = 2
        else:
            self.sprite_index = 3
            if self.ticker > 3:
                self.sprite_index = 4
            if self.ticker > 7:
                self.sprite_index = 3
            if self.ticker > 11:
                self.sprite_index = 5
                
    def get_sprite(self):
        return self.sprites[self.sprite_index]