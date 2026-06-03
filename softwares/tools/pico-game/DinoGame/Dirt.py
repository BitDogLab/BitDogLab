class Dirt:
    def __init__(self, x, y, vx):
        self.x = x
        self.y = y
        self.vx = vx
        self.sprite_index = 0
        self.sprites = []
    
    def update(self):
        # move the Cactus
        # at speed vx
        self.x -= self.vx
        if self.x < -8:
            self.x = 128
            self.sprite_index += 1
            if self.sprite_index >= len(self.sprites):
                self.sprite_index = 0
                
    def get_sprite(self):
        return self.sprites[self.sprite_index]