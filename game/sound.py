import pygame as pg

class Sound:
    def __init__(self,game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sounds/'
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.npc_damage = pg.mixer.Sound(self.path + 'npc_damage.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_attack = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.player_damage = pg.mixer.Sound(self.path + 'player_damage.wav')