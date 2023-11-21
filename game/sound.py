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
        self.npc_attack.set_volume(0.2)
        self.player_damage = pg.mixer.Sound(self.path + 'player_damage.wav')
        self.music = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.3)