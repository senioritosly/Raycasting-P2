import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_img = self.get_textures('./resources/textures/sky.jpg', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_textures('./resources/textures/player_damage.png', RES)
        self.number_size = 90
        self.number_images = [self.get_textures(f'./resources/textures/numbers/{i}.png', [self.number_size] * 2)
                              for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.number_images))
        self.game_over_image = self.get_textures('./resources/textures/game_over.png', RES)

    def draw(self):
        self.draw_bg()
        self.render_game_objects()
        self.draw_health()
    
    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.number_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.number_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_bg(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_img, (-self.sky_offset, 0))
        self.screen.blit(self.sky_img, (WIDTH - self.sky_offset, 0))
        # piso
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda x: x[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_textures(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_textures('./resources/textures/wall1.png'),
            2: self.get_textures('./resources/textures/wall2.png'),
            3: self.get_textures('./resources/textures/wall3.png'),
        }