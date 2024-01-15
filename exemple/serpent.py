from pygame import *
a = 1080
b = 720
c = 160*4
d = 64
class S1:
    def __init__(self, x, y):
        self.image = image.load('serpent_droit_tete.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S2:
    def __init__(self, x, y):
        self.image = image.load('serpent_bas_tete.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S3:
    def __init__(self, x, y):
        self.image = image.load('serpent_droite_tete.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S4:
    def __init__(self, x, y):
        self.image = image.load('serpent_gauche_tete.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S5:
    def __init__(self, x, y):
        self.image = image.load('serpent_haut_queue_milieu.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S6:
    def __init__(self, x, y):
        self.image = image.load('serpent_droit_queue_milieu.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S7:
    def __init__(self, x, y):
        self.image = image.load('serpent_bas_queue_fin.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S8:
    def __init__(self, x, y):
        self.image = image.load('serpent_haut_queue_fin.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S9:
    def __init__(self, x, y):
        self.image = image.load('serpent_gauche_queue_fin.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S10:
    def __init__(self, x, y):
        self.image = image.load('serpent_droit_queue_fin.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S11:
    def __init__(self, x, y):
        self.image = image.load('bas_droite.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S12:
    def __init__(self, x, y):
        self.image = image.load('serpent_milieu_plier.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S13:
    def __init__(self, x, y):
        self.image = image.load('gauche_haut.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
class S14:
    def __init__(self, x, y):
        self.image = image.load('ExportedLayers.png')
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.rect.x = self.x * 64 + (a - c) / 2 - d / 2
        self.rect.y = self.y * 64 + (b - c) / 2 - d / 2
