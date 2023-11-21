from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'resources/sprites/static/'
        self.animated_sprite_path = 'resources/sprites/animated/'
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(AnimatedSprite(game, pos=(13.25, 1.25)))
        add_sprite(AnimatedSprite(game, pos=(14.85, 1.25)))
        add_sprite(AnimatedSprite(game, pos=(1.15, 1.25)))
        add_sprite(AnimatedSprite(game, pos=(1.15, 1.75)))
        add_sprite(AnimatedSprite(game, pos=(1.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(2.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(3.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(4.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(5.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(6.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(7.15, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(8.15, 7.85)))
        add_sprite(SpriteObject(game, pos=(1.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(2.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(3.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(4.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(5.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(6.65, 7.85)))
        add_sprite(SpriteObject(game, pos=(7.65, 7.85)))
        add_sprite(AnimatedSprite(game, pos=(14.75, 7.5)))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)