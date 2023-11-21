from sprite_object import *
from random import randint, random, choice

class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(14.0, 1.25),
                 scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.damage_images = self.get_images(self.path + '/damage')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(1, 3)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.damage = False
        self.ray_cast_value = False

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        self.draw_ray_cast()

    def animate_damage(self):
        self.animate(self.damage_images)
        if self.animation_trigger:
            self.damage = False

    def check_hit_npc(self):
        if self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.sound.npc_damage.play()
                self.game.player.shot = False
                self.damage = True

    def run_logic(self):
        if self.alive:
            self.check_hit_npc()
            if self.damage:
                self.animate_damage()
            else:
                self.animate(self.idle_images)

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta
        
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        # horizontals
        y_horz, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
        depth_horz = (y_horz - oy) / sin_a
        x_horz = ox + depth_horz * cos_a
        delta_depth = dy / sin_a
        dx = delta_depth * cos_a
        for i in range(MAX_DEPTH):
            tile_horz = int(x_horz), int(y_horz)
            if tile_horz == self.map_pos:
                player_dist_h = depth_horz
                break
            if tile_horz in self.game.map.world_map:
                wall_dist_h = depth_horz
                break
            x_horz += dx
            y_horz += dy
            depth_horz += delta_depth
        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a
        delta_depth = dx / cos_a
        dy = delta_depth * sin_a
        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
    
    def draw_ray_cast(self):
        pg.draw.circle(self.game.screen, 'red', (100 * self.x, 100 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y),
                         (100 * self.x, 100 * self.y), 2)