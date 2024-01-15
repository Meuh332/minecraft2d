print("importation des module dans joueur")
from pygame import *
from inventaire import Inventaire
print("importation des module dans joueur terminé")
print("initialisation de la classe joueur")


class Player:
    def __init__(self):
        self.image = image.load("textures/entity/player/steved.png")
        self.vie = 100
        self.vitesse = 10
        self.saut = 25
        self.sautc = self.saut
        self.rect = self.image.get_rect()
        self.rect.x = 1080 / 2 - 22
        self.rect.y = 720 / 2 - 170 / 2
        self.inv = Inventaire()


print("initialisation de la classe joueur terminée")
