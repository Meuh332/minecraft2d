print("importation des module pour l'inventaire")
from pygame import *
from blockimage import block
from blocklistfile import blocklist, blockattrlist
print("importation des module pour l'inventaire terminé")

print("initialisation de l'inventaire")
class Inventaire:
    def __init__(self):
        self.hotbarimage = image.load("textures/interface/hotbar2.png")
        self.hotbarrect = self.hotbarimage.get_rect()
        self.hotbarrect.x = 1080 / 2 - 434 / 2
        self.hotbarrect.y = 720 / 2 + 250
        self.image = image.load("textures/interface/inventaire.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1080 / 2 - 400 / 2
        self.rect.y = 720 / 2 - 400 / 2
        self.itemselected = [[0, 0], False]
        self.inventaire = [
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[1, 1], [6, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        ]
        xl = 0
        yl = 0
        for i in self.inventaire:
            for i2 in i:
                try:
                    self.inventaire[yl][xl][0] = blockattrlist[blocklist[self.inventaire[yl][xl][0]]]
                except Exception as e:
                    print(blocklist[len(blocklist) - 1])
                    print(f"Erreur lors du chargement d'un item : {e}")
                    self.inventaire[yl][xl][0] = blockattrlist["air"]
                    self.inventaire[yl][xl][1] = 0
                if self.inventaire[yl][xl][0] == 0:
                    print("non")
                xl += 1
            yl += 1
            xl = 0
        self.invpos = [
            [[360, 425], [406, 425], [452, 425], [499, 425], [545, 425], [591, 425], [637, 425], [683, 425],
             [728, 425]],
            [[360, 475], [406, 475], [452, 475], [499, 475], [545, 475], [591, 475], [637, 475], [683, 475],
             [728, 475]],
            [[360, 522], [406, 522], [452, 522], [499, 522], [545, 522], [591, 522], [637, 522], [683, 522],
             [728, 522]],
            [[360, 583], [406, 583], [452, 583], [499, 583], [545, 583], [591, 583], [637, 583], [683, 583], [728, 583]]
        ]
        # [class, quant]

    def give(self, item):
        hotbarslot = False
        okey = False
        p = False
        invxx = 0
        for invx in self.inventaire[3]:
            if invx[0] == item:
                if invx[1] != 64 and not p:
                    invx[1] += 1
                    okey = True
                    p = True
            invxx += 1
        okey2 = False
        p2 = p
        if not okey:
            invxx = 0
            for invx in self.inventaire[3]:
                if invx[0].block == 0 and not p2:
                    if item != 0:
                        invx[0] = item
                        invx[1] += 1
                        okey2 = True
                        p2 = True
                invxx += 1
        if not okey and not okey2:
            hotbarslot = False
        else:
            hotbarslot = True
        if not hotbarslot:
            okey = False
            p = False
            invyy = 0
            for invy in self.inventaire:
                invxx = 0
                for invx in invy:
                    if invx[0] == item:
                        if invx[1] != 64 and not p:
                            invx[1] += 1
                            okey = True
                            p = True
                    invxx += 1
                invyy += 1
            okey2 = False
            p2 = p
            if not okey:
                invyy = 0
                for invy in self.inventaire:
                    invxx = 0
                    for invx in invy:
                        if invx[0] == 0 and not p2:
                            if item != 0:
                                invx[0] = item
                                invx[1] += 1
                                okey2 = True
                                p2 = True
                        invxx += 1
                    invyy += 1
            if not okey and not okey2:
                return False
            else:
                return True
        return True

    def ungive(self, pos: tuple[int, int], quant: int = 1):
        ob = self.inventaire[pos[0]][pos[1]]
        if ob[1] < quant or ob[0] == 0:
            return False
        else:
            self.inventaire[pos[0]][pos[1]][1] -= quant
            if self.inventaire[pos[0]][pos[1]][1] == 0:
                self.inventaire[pos[0]][pos[1]][0] = blockattrlist["air"]
            return True

    def affhotbar(self, screen):
        invxx = 0
        for invx in self.inventaire[3]:
            b, isok = block(invx[0])
            if not isok:
                self.inventaire[3][invxx] = [0, 0]
            if invx[0] != 0:
                br = b.get_rect()
                br.x = self.invpos[3][invxx][0] - 25
                br.y = self.invpos[3][invxx][1] + 38
                screen.blit(b, br)
            invxx += 1

            if invx[1] != 0 and invx[1] < 10:
                b = image.load("textures/caractère/0.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 10 <= invx[1] < 20:
                b = image.load("textures/caractère/1.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 20 <= invx[1] < 30:
                b = image.load("textures/caractère/2.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 30 <= invx[1] < 40:
                b = image.load("textures/caractère/3.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 40 <= invx[1] < 50:
                b = image.load("textures/caractère/4.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 50 <= invx[1] < 60:
                b = image.load("textures/caractère/5.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            if 60 <= invx[1] < 70:
                b = image.load("textures/caractère/6.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] - 5
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)
            u = invx[1] % 10
            if invx[1] != 0:
                b = image.load(f"textures/caractère/{str(u)}.png")
                br = b.get_rect()
                br.x = self.invpos[3][invxx - 1][0] + 10
                br.y = self.invpos[3][invxx - 1][1] + 65
                screen.blit(b, br)

# 380 362
print("initialisation de l'inventaire trminé")