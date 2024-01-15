import os

print("importation des modules")
import pygame
from pygame import *
from world import w, visible_blocks
from pygame import *
from player import Player
from random import *
from time import *
from inventaire import Inventaire
from blockimage import block
import blocklistfile

print("importation des modules terminé")

print("inatialisation de la fenêtre")
pygame.init()
display.set_caption("minecraft 2d")
screen = display.set_mode((1080, 720))
print("inatialisation de la fenêtre terminée")

print("initalisation des variables")
false = False
true = True

grav = 0
gravmax = 25

keys = []
on = True
p = Player()
saut = False
inv = False
bouton = None
c = False
clicx = 0
clicy = 0
cassage = False
framec = []
frames_casse_index = 0
invswitch = False
camerax = 0
cameray = 0
gmx = 0
gmy = 0
gmxp = 0
gmyp = 0
axp = 0
ayp = 0
h = 12
selectedslot = 0
boutonswitch = bouton
casssval = 0
gui = ""
indepinv = False
actumpos = [0, 0]
print("initalisation des variables terminée")

print("initalisation des fonction")

casse_animation_frames = []
for i in range(1, 5):
    image = pygame.image.load(f"textures/blocks/c{i}.png")
    casse_animation_frames.append(image)


def listvarfoncretour(l):
    global keys, saut, inv, bouton, c, clicx, clicy, cassage, framec, frames_casse_index, invswitch, camerax, cameray, gmx, gmy, gmyp, gmxp, axp, ayp, h, selectedslot, boutonswitch, casssval, gui, indepinv
    keys = l["keys"]
    saut = l["saut"]
    inv = l["inv"]
    bouton = l["bouton"]
    c = l["c"]
    clicx = l["clicx"]
    clicy = l["clicy"]
    cassage = l["cassage"]
    framec = l["framec"]
    frames_casse_index = l["frames_casse_index"]
    invswitch = l["invswitch"]
    camerax = l["camerax"]
    cameray = l["cameray"]
    gmx = l["gmx"]
    gmy = l["gmy"]
    gmxp = l["gmxp"]
    gmyp = l["gmyp"]
    axp = l["axp"]
    ayp = l["ayp"]
    h = l["h"]
    selectedslot = l["selectedslot"]
    boutonswitch = l["boutonswitch"]
    casssval = l["casssval"]
    gui = l["gui"]
    indepinv = l["indepinv"]


def listvarfonc():
    var = {
        "keys": keys,
        "saut": saut,
        "inv": inv,
        "bouton": bouton,
        "c": c,
        "clicx": clicx,
        "clicy": clicy,
        "cassage": cassage,
        "framec": framec,
        "frames_casse_index": frames_casse_index,
        "invswitch": invswitch,
        "camerax": camerax,
        "cameray": cameray,
        "gmx": gmx,
        "gmy": gmy,
        "gmxp": gmxp,
        "gmyp": gmyp,
        "axp": axp,
        "ayp": ayp,
        "h": h,
        "selectedslot": selectedslot,
        "boutonswitch": boutonswitch,
        "casssval": casssval,
        "gui": gui,
        "indepinv": indepinv
    }
    return var


def btn(x: int, n: int):
    if x == n:
        return 0, True
    else:
        return x + 1, False


def get_activemodbool():
    modfile = open("mods/parameter.config", "r")
    listn1 = modfile.read().split("\n")
    modload = {}
    for i in listn1:
        nt = i.split("=")
        modload[nt[0]] = nt[1]
    if modload["active"] == "True":
        return True
    else:
        return False


def get_activemod():
    activemod = []
    for file in os.listdir("mods/mods"):
        try:
            if file.endswith(".py"):  # S'assure que le fichier est un script Python
                module_name = file[:-3]  # Retire l'extension .py
                mod = __import__("mods.mods." + module_name, fromlist=[''])
                # battrsupmod, blistsupmod = mod.get_blocks()
                if mod.active:
                    activemod.append(mod)
        except Exception as e:
            print("huh")
            print(f"Erreur lors du chargement du module {file}: {e}")
    return activemod


def aff(self, pos: tuple[tuple[int, int], tuple[int:int]]):
    invyy = 0
    for invy in self.inventaire:
        invxx = 0
        for invx in invy:
            if invx[0] == 0:
                invx[1] = 0
            b, isok = block(invx[0])
            if not isok:
                self.inventaire[invyy][invxx] = [0, 0]
            if p.inv.itemselected[0] != [invyy, invxx]:
                if invx[0] != 0:
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0] + pos[0][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[0][1]
                    screen.blit(b, br)
                if invx[1] != 0 and invx[1] < 10:
                    b = image.load("textures/caractère/0.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 10 <= invx[1] < 20:
                    b = image.load("textures/caractère/1.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 20 <= invx[1] < 30:
                    b = image.load("textures/caractère/2.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 30 <= invx[1] < 40:
                    b = image.load("textures/caractère/3.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 40 <= invx[1] < 50:
                    b = image.load("textures/caractère/4.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 50 <= invx[1] < 60:
                    b = image.load("textures/caractère/5.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
                if 60 <= invx[1] < 70:
                    b = image.load("textures/caractère/6.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]

                    screen.blit(b, br)
                u = invx[1] % 10
                if invx[1] != 0:
                    b = image.load(f"textures/caractère/{str(u)}.png")
                    br = b.get_rect()
                    br.x = self.invpos[invyy][invxx][0] + pos[1][0]
                    br.y = self.invpos[invyy][invxx][1] + pos[1][1]
                    screen.blit(b, br)
            else:
                if invx[0] != 0:
                    br = b.get_rect()
                    b, br = changetailleimage(b, (120, 120), True)
                    br.x = actumpos[0] - b.get_size()[0] // 2
                    br.y = actumpos[1] - b.get_size()[1] // 2
                    screen.blit(b, br)
                if invx[1] != 0 and invx[1] < 10:
                    b = image.load("textures/caractère/0.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 10 <= invx[1] < 20:
                    b = image.load("textures/caractère/1.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 20 <= invx[1] < 30:
                    b = image.load("textures/caractère/2.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 30 <= invx[1] < 40:
                    b = image.load("textures/caractère/3.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 40 <= invx[1] < 50:
                    b = image.load("textures/caractère/4.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 50 <= invx[1] < 60:
                    b = image.load("textures/caractère/5.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
                if 60 <= invx[1] < 70:
                    b = image.load("textures/caractère/6.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 20
                    br.y = actumpos[1] - 20

                    screen.blit(b, br)
                u = invx[1] % 10
                if invx[1] != 0:
                    b = image.load(f"textures/caractère/{str(u)}.png")
                    br = b.get_rect()
                    br.x = actumpos[0] - 5
                    br.y = actumpos[1] - 20
                    screen.blit(b, br)
            invxx += 1
        invyy += 1


def changetailleimage(img: pygame.image, ntaille: tuple[int, int], ispersentage: bool = False):
    t = img.get_size()
    mt = [100, 100]
    mi = img
    nr = mi.get_rect()
    if ispersentage:
        mt[0] = t[0] / 100 * ntaille[0]
        mt[1] = t[1] / 100 * ntaille[1]
        mi = transform.scale(img, mt)
        nr = mi.get_rect(center=nr.center)
    else:
        mi = transform.scale(img, ntaille)
        nr = mi.get_rect(center=nr.center)
    return mi, nr


def t(t):
    for u in keys:
        if t == u:
            return true
    return false


def toutch(x, y):
    # Arrondir les coordonnées aux multiples de 44
    x += camerax
    y += cameray
    x = int(x / 44) * 44
    y = int(y / 44) * 44

    # Convertir les coordonnées en indices de la matrice
    x = x // 44
    y = y // 44

    # Vérifier si la case dans la matrice est différente de zéro (si c'est un bloc)
    if x > -1 and y > -1:
        try:
            if w[y][x].block != 0:
                return True
        except IndexError:
            return False
    else:
        return False


def toutchp(x, y):
    x = int(x / 44) * 44
    y = int(y / 44) * 44

    # Convertir les coordonnées en indices de la matrice
    x = x // 44
    y = y // 44

    # Vérifier si la case dans la matrice est différente de zéro (si c'est un bloc)
    if x > -1 and y > -1:
        try:
            return w[y][x]
        except IndexError:
            return 0
    else:
        return 0


def coo(x, y):
    x = int(x / 44) * 44
    y = int(y / 44) * 44

    # Convertir les coordonnées en indices de la matrice
    x = x // 44
    y = y // 44

    # Vérifier si la case dans la matrice est différente de zéro (si c'est un bloc)
    return x, y


def gmp(gmx):
    c = 0
    while gmx - 44 >= 0:
        c += 1
        gmx -= 44
    return c


def checkdepitems(posm: tuple[tuple[int, int], tuple[int, int]], inv=True):
    if gui != "":
        if boutonswitch == "g" and not p.inv.itemselected[1]:
            if posm[0][0] > clicx - camerax > posm[0][1] and posm[1][0] > clicy - cameray > posm[1][1]:
                depguix = (clicx - camerax - posm[0][1]) // 44
                depguiy = 0
                if inv:
                    depguiy = (clicy - cameray - posm[1][1])
                    if depguix > 8:
                        depguix = 8
                    if depguiy < 45:
                        depguiy = 0
                    elif 95 > depguiy > 44:
                        depguiy = 1
                    elif 144 > depguiy > 95:
                        depguiy = 2
                    elif 159 > depguiy > 144:
                        depguiy = -1
                    elif depguiy > 159:
                        depguiy = 3
                    else:
                        depguiy = -1
                else:
                    depguiy = (clicy - cameray - 386) // 44
                if p.inv.inventaire[depguiy][depguix][0].block != 0:
                    p.inv.itemselected[0] = [depguiy, depguix]
                    p.inv.itemselected[1] = True

        elif p.inv.itemselected[1] and boutonswitch == "g":
            if posm[0][0] > clicx - camerax > posm[0][1] and posm[1][0] > clicy - cameray > posm[1][1]:
                depguix2 = (clicx - camerax - posm[0][1]) // 44
                depguiy2 = (clicy - cameray - posm[1][1])
                if depguix2 > 8:
                    depguix2 = 8
                if depguiy2 < 45:
                    depguiy2 = 0
                elif 95 > depguiy2 > 44:
                    depguiy2 = 1
                elif 144 > depguiy2 > 95:
                    depguiy2 = 2
                elif 159 > depguiy2 > 144:
                    depguiy2 = -1
                elif depguiy2 > 159:
                    depguiy2 = 3
                else:
                    depguiy2 = -1
                # print(depguix2, p.inv.itemselected[0][1])
                # print(p.inv.inventaire[depguiy2][depguix2][0].block)
                # print([depguiy2])
                if p.inv.inventaire[depguiy2][depguix2][0].block == 0 or [depguiy2, depguix2] == p.inv.itemselected[0]:

                    p.inv.inventaire[depguiy2][depguix2][0] = \
                        p.inv.inventaire[p.inv.itemselected[0][0]][p.inv.itemselected[0][1]][0]
                    p.inv.inventaire[depguiy2][depguix2][1] = \
                        p.inv.inventaire[p.inv.itemselected[0][0]][p.inv.itemselected[0][1]][1]
                    if not [depguiy2, depguix2] == p.inv.itemselected[0]:
                        p.inv.inventaire[p.inv.itemselected[0][0]][p.inv.itemselected[0][1]] = [
                            blocklistfile.blockattrlist[blocklistfile.blocklist[0]], 0]
                    p.inv.itemselected = [[-1, -1], False]

                else:
                    pos = p.inv.itemselected[0]
                    depco = [depguiy2, depguix2]
                    rien = blocklistfile.blockattrlist[blocklistfile.blocklist[0]]

                    a = p.inv.inventaire[pos[0]][pos[1]]
                    b2 = p.inv.inventaire[depco[0]][depco[1]]

                    c2 = a
                    a = b2
                    b2 = c2
                    p.inv.inventaire[depco[0]][depco[1]] = b2
                    p.inv.inventaire[pos[0]][pos[1]] = a

                    p.inv.itemselected = [pos, True]
        # print(p.inv.itemselected[1])
    else:
        p.inv.itemselected = [[0, 0], False]

    # print(p.inv.itemselected)
    # print(actumpos)


print("initalisation des fonction terminée")

print("setup")
# setup --------------------------------------------------
screen.fill((0, 100, 255))
# p.inv.give(7)
# blocklistfile.check_mod()
# setup --------------------------------------------------
print("setup terminé")

print("importation d'un module déplacé suite à des problème")
from pygame import *

print("importation du module déplacé suite à des problème terminé")

while on:
    w2 = w  # visible_blocks(camerax, cameray, 1080, 720)
    for event in pygame.event.get():
        if event.type == QUIT:
            on = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Bouton gauche de la souris
                bouton = "g"
                c = True
                clicx, clicy = event.pos
                clicx += camerax
                clicy += cameray
                if not inv and not cassage:
                    framec = casse_animation_frames
                    frames_casse_index = 0
                    cassage = True
            elif event.button == 3:  # Bouton droit de la souris
                bouton = "d"
                c = True
                clicx, clicy = event.pos
                clicx += camerax
                clicy += cameray
            boutonswitch = bouton
        if event.type == MOUSEBUTTONUP:
            c = False
            cassage = False
            framec = []
        if event.type == KEYDOWN:
            keys.append(event.key)
        if event.type == KEYUP:
            for k in keys:
                if k == event.key:
                    keys.remove(event.key)
        if event.type == MOUSEWHEEL:
            if event.y == 1:
                if selectedslot == 0:
                    selectedslot = 8
                else:
                    selectedslot -= 1
            if event.y == -1:
                if selectedslot == 8:
                    selectedslot = 0
                else:
                    selectedslot += 1
        if event.type == MOUSEMOTION:
            actumpos = event.pos
    screen.fill((0, 100, 255))
    mcy = 0
    var = True

    for my in w:
        mcx = 0
        for mx in my:
            if mx.block != 0:
                b, isok = block(mx)
                if not isok:
                    w[mcy][mcx] = blocklistfile.blockattrlist["air"]
                br = b.get_rect()
                br.x = mcx * 44 - camerax
                br.y = mcy * 44 - cameray

                screen.blit(b, br)
            mcx += 1
        mcy += 1
    # grav --------------------------------------------------
    grav += 1
    cameray += grav
    if toutch(p.rect.x + 5, p.rect.y + 170) or toutch(p.rect.x + 39, p.rect.y + 170) or toutch(p.rect.x,
                                                                                               p.rect.y + 44) or toutch(
        p.rect.x + 44, p.rect.y + 44):  # Vérifier la collision avec le bloc en dessous
        p.sautc = p.saut  # Réinitialiser le compteur de saut
        cameray -= grav  # Remettre le joueur au-dessus du bloc en dessous
        grav = 0  # Réinitialiser la gravité ici (mettre à zéro)
        saut = False

    # /grav -------------------------------------------------

    # ctrl --------------------------------------------------
    p.vx = 0  # Réinitialiser la vitesse horizontale du joueur

    if t(K_d) and not toutch(p.rect.x + p.rect.width, p.rect.y + 5) and not toutch(
            p.rect.x - 10 + p.rect.width, p.rect.y + p.rect.height - 88) and not toutch(
        p.rect.x - 10 + p.rect.width, p.rect.y + p.rect.height - 132) and not toutch(
        p.rect.x - 10 + p.rect.width, p.rect.y + p.rect.height - 44):
        p.vx = p.vitesse  # Définir la vitesse horizontale du joueur vers la droite
        p.image = image.load("textures/entity/player/steved.png")

    if t(K_a) and not toutch(p.rect.x - 5, p.rect.y + 5) and not toutch(
            p.rect.x, p.rect.y + p.rect.height - 88) and not toutch(
        p.rect.x, p.rect.y + p.rect.height - 132) and not toutch(
        p.rect.x, p.rect.y + p.rect.height - 44):
        p.vx = -p.vitesse  # Définir la vitesse horizontale du joueur vers la gauche
        p.image = image.load("textures/entity/player/steveg.png")

    camerax += p.vx
    gmx += p.vx

    sp = False
    if toutch(p.rect.x + 5, p.rect.y + p.rect.height) or toutch(p.rect.x + 39, p.rect.y + p.rect.height):
        sp = True
    if t(K_SPACE) and sp:
        saut = True
    if saut and not toutch(p.rect.x + 5, p.rect.y + 1) and not toutch(p.rect.x + 39, p.rect.y + 1):
        cameray -= p.sautc
        p.sautc -= 1
    if toutch(p.rect.x + 5, p.rect.y) or toutch(p.rect.x + 39, p.rect.y):
        p.sautc = p.saut
        cameray += p.sautc - 5
        saut = False
    if toutch(p.rect.x + 5, p.rect.y + p.rect.height) or toutch(p.rect.x + 39, p.rect.y + p.rect.height):
        saut = False
        p.sautc = p.saut
    if t(K_e) and not invswitch:
        if inv:
            inv = False
            gui = ""
        else:
            if gui == "":
                inv = True
                gui = "inv"
    if t(K_ESCAPE) and not invswitch:
        if inv:
            inv = False
    if t(K_e):
        invswitch = True
    else:
        invswitch = False

    if t(K_ESCAPE) or (t(K_e) and not inv):
        gui = ""
    # /ctrl -------------------------------------------------
    # casser -----------------------------------------------
    if not gui and c and bouton == "g":
        cassex = int(clicx / 44) * 44
        cassey = int(clicy / 44) * 44
        cassex = cassex // 44
        cassey = cassey // 44
        try:
            if w[cassey][cassex].block != 0:
                if get_activemodbool():
                    for mod in get_activemod():
                        if mod.clicg:
                            for i in mod.blockattrlist:
                                mod.clicgf(p.inv.inventaire[3][selectedslot], (clicx, clicy), p, w[cassey][cassex],
                                           listvarfonc())
        except Exception as ero:
            print("éreur ou trop loin err:", ero)
        if len(framec) != 0:
            cimage = framec[
                frames_casse_index]  # Utilisez frames_casse[frames_casse_index] au lieu de frames_casse.pop(0)
            cc = cimage.get_rect()
            cc.x = cassex * 44 - camerax
            cc.y = cassey * 44 - cameray
            try:
                if w[cassey][cassex].block != 0:
                    screen.blit(cimage, cc)
            except:
                print("trop loin")

            if type(toutchp(clicx, clicy)) != int:
                if type(toutchp(clicx, clicy).block) == int:
                    casssval, don = btn(casssval,
                                        blocklistfile.blockattrlist[
                                            blocklistfile.blocklist[toutchp(clicx, clicy).block]].resistance)
                    if don:
                        if blocklistfile.blockattrlist[blocklistfile.blocklist[toutchp(clicx, clicy).block]].cassable:
                            frames_casse_index += 1  # Augmentez l'index pour passer à la prochaine image de l'animation

            if frames_casse_index >= len(framec):
                cassage = False  # Réinitialisez l'animation de casse lorsque toutes les textures ont été affichées
                frames_casse_index = 0
                try:
                    if not w[cassey][cassex].block == 0:
                        if blocklistfile.blockattrlist[blocklistfile.blocklist[toutchp(clicx, clicy).block]].handrecup:
                            p.inv.give(
                                blocklistfile.blockattrlist[blocklistfile.blockattrlist[
                                    blocklistfile.blocklist[toutchp(clicx, clicy).block]].recup[1]]
                            )
                            # print(blocklistfile.blockattrlist[blocklistfile.blockattrlist[blocklistfile.blocklist[toutchp(clicx, clicy).block]].recup[1]].imagename)
                        w[cassey][cassex] = blocklistfile.blockattrlist["air"]

                except Exception as er:
                    print("trop loin", er)

        if len(framec) == 0:
            cassage = False
            casssval = 0
    else:
        cassage = False
        casssval = 0
    # /casser -----------------------------------------------
    # poser ---------------------------------------
    if clicx is not None and clicy is not None:
        if toutchp(clicx, clicy) != 0:
            if toutchp(clicx, clicy).block == 0:
                if c and boutonswitch == "d":
                    posimgchaeckco = list(coo(clicx, clicy))
                    posimgchaeckco[0] *= 44
                    posimgchaeckco[1] *= 44
                    posimgchaeckco[0] -= camerax
                    posimgchaeckco[1] -= cameray
                    posimgcheckimg = image.load("textures/blocks/air.png")
                    posimgcheckrect = posimgcheckimg.get_rect()
                    posimgcheckrect.x = posimgchaeckco[0]
                    posimgcheckrect.y = posimgchaeckco[1]
                    if not p.rect.colliderect(posimgcheckrect) and gui == "":
                        if p.inv.inventaire[3][selectedslot][0] != 0:
                            try:
                                w[coo(clicx, clicy)[1]][coo(clicx, clicy)[0]] = p.inv.inventaire[3][selectedslot][0]
                                p.inv.ungive((3, selectedslot))
                                boutonswitch = ""
                            except:
                                print("trop loin")
            else:
                if c and boutonswitch == "d":
                    if get_activemodbool():
                        for mod in get_activemod():
                            if mod.clicd:
                                for i in mod.blockattrlist:
                                    mod.clicdf(p.inv.inventaire[3][selectedslot], (clicx, clicy), p,
                                               toutchp(clicx, clicy), listvarfonc())
    # /poser ----------------------------------------
    # gui ---------------------------------------
    if clicx is not None and clicy is not None:
        if blocklistfile.blockattrlist[blocklistfile.blocklist[toutchp(clicx, clicy).block]].gui:
            if c and boutonswitch == "d" and gui == "":
                if toutchp(clicx, clicy).block == 6:
                    gui = "craft"
    # /gui -------------------------------------
    screen.blit(p.image, p.rect)
    if inv:
        screen.blit(p.inv.image, p.inv.rect)
        aff(p.inv, ((0, -39), (15, -39)))
    if gui == "craft":
        i = image.load("textures/interface/craftingtable.png")
        ir = i.get_rect()
        screen.blit(i, ir)
        aff(p.inv, ((-20, 73), (15, 73)))
        checkdepitems(((755, 335), (703, 498)))
        #draw.line(screen, (0, 0, 0), (335, 498), (755, 703))
        print(clicx, clicy)
    if gui == "inv" or gui == "":
        screen.blit(p.inv.hotbarimage, p.inv.hotbarrect)
        seleimg = image.load("textures/interface/selected.png")
        selerect = seleimg.get_rect()
        selerect.x = 1080 / 2 - 434 / 2 + 44 * selectedslot + 2 * selectedslot - 1
        selerect.y = 1080 / 2 + 66
        p.inv.affhotbar(screen)
        screen.blit(seleimg, selerect)
        checkdepitems(((769, 360), (590, 386)))
        #draw.line(screen, (0, 0, 0), (360, 386), (769, 590))
    if get_activemodbool():
        for mod in get_activemod():
            l = mod.mainf(p, listvarfonc(), screen)
            listvarfoncretour(l)
    display.flip()
    boutonswitch = ""
    sleep(1 / 100)
