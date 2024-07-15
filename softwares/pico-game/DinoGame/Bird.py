class Bird:
    def __init__(self):
        self.x = 256
        self.y = 20
        self.sprite_index = 0
        self.timer = 20
        self.sprites = []
                
    def update(self):
        # move the Cactus
        # at speed vx
        self.x -= 1
        if self.x < -32:
            self.x = 256
        self.timer -= 1
        if self.timer == 0:
            self.timer = 20
            self.sprite_index = 1 - self.sprite_index
            
    def get_sprite(self):
        return self.sprites[self.sprite_index]