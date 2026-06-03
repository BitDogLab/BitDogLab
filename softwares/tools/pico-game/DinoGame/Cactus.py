class Cactus:
    def __init__(self):
        self.x = 128
        self.y = 35
        self.sprite_index = 0
        self.sprites = []

    def update(self):
        # move the Cactus
        # at speed vx
        self.x -= 1
        if self.x < -32:
            self.x = 128
    
    def get_sprite(self):
        return self.sprites[self.sprite_index]
